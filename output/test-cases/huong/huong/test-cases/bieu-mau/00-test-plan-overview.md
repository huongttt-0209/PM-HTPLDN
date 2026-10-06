# Kế Hoạch Kiểm Thử — Thư viện Biểu mẫu, Hợp đồng (FR-VII, SCR-VII-01..03)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-06
> **Nguồn dữ liệu**: SRS v3.5 ([srs-fr-09-bieu-mau-v3.1.md](../../../input/srs-v3/srs-fr-09-bieu-mau-v3.1.md), kèm [srs-v3.md](../../../input/srs-v3/srs-v3.md) cho BR Phụ lục B)
> **SRS Reference**: Nhóm VII (FR-VII-01..07), SCR-VII-01/02/03, Entity BIEU_MAU + THU_MUC_BIEU_MAU + FILE_DINH_KEM
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho module Thư viện Biểu mẫu. FR-VII-07 (API thuần cho Cổng PLQG) **LOẠI** per A7 filter rule (require curl/Postman — không có UI). FR-VII-08 đã chuyển sang `srs-fr-14-hop-dong-tv.md`.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử
- 6 FR (UC92–UC97) trên 3 màn hình. **FR-VII-07 (UC98 API) LOẠI (A7 — API thuần, không UI). FR-VII-08 đã chuyển sang FR-14.**
- Entity chính: `THU_MUC_BIEU_MAU` (owned), `BIEU_MAU` (owned), `FILE_DINH_KEM` (referenced)
- Màn hình: SCR-VII-01 (Quản lý Thư mục), SCR-VII-02 (Quản lý Biểu mẫu), SCR-VII-03 (Import hàng loạt)
- State Machine: SM-BIEUMAU: `NHAP → CONG_KHAI ⟷ AN`, `NHAP/AN → XOA`
- Đặc thù: Công khai **KHÔNG cần phê duyệt** (BR-FLOW-07). CR-01 thêm 4 field công khai (Switch, ảnh đại diện, mô tả công khai, file đính kèm công khai).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-VII-01 | UC92 | Quản lý thư mục biểu mẫu (CRUD) | THU_MUC_BIEU_MAU | `01-TC-quan-ly-thu-muc.md` |
| 2 | FR-VII-02 | UC93 | Tìm kiếm thư mục biểu mẫu | THU_MUC_BIEU_MAU | `02-TC-tim-kiem-thu-muc.md` |
| 3 | FR-VII-03 | UC94 | Công khai thư mục lên Cổng PLQG | THU_MUC_BIEU_MAU | `03-TC-cong-khai-thu-muc.md` |
| 4 | FR-VII-04 | UC95 | Quản lý biểu mẫu (CRUD + file upload + preview + download + CR-01 công khai) | BIEU_MAU, FILE_DINH_KEM | `04-TC-quan-ly-bieu-mau.md` |
| 5 | FR-VII-05 | UC96 | Tìm kiếm biểu mẫu | BIEU_MAU | `05-TC-tim-kiem-bieu-mau.md` |
| 6 | FR-VII-06 | UC97 | Import biểu mẫu hàng loạt | BIEU_MAU, FILE_DINH_KEM | `06-TC-import-hang-loat.md` |
| 7 | — | — | Permission matrix (cross-FR-VII) | All | `07-TC-permission-matrix.md` |
| ~~8~~ | ~~FR-VII-07~~ | ~~UC98~~ | ~~API chia sẻ biểu mẫu~~ — **LOẠI A7 (API thuần)** | — | — |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (toàn HT). `_02` fallback |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD primary (scope TW = toàn quốc). `_02` fallback, `_03` permission test |
| CB_NV_BN | BN | cb_nv_bn_01 (Bộ KH&ĐT) | CRUD scoped BN |
| CB_NV_DP | DP | cb_nv_dp_01 (Sở TP AG) | CRUD scoped ĐP. `_02` Sở TP BG |
| CB_PD_TW | TW | cb_pd_tw_01 | Read-only (tìm kiếm thư mục/BM). KHÔNG CRUD |
| CB_PD_BN | BN | cb_pd_bn_01 | Read-only scoped BN |
| CB_PD_DP | DP | cb_pd_dp_01 | Read-only scoped ĐP |
| NHT/TVV/CG/DN/GV | — | nht_01, tvv_01, cg_01, dn_01 | Negative — verify 403 chặn module |

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> **Footnote convention (Codex 2026-05-09):**
> - **BR formal §6 srs-fr-09**: Authoritative BR declared in SRS FR-VII §6 (lines 859-937). Có 11 BR: BR-AUTH-01/08, BR-DATA-01/03/05/07, BR-FLOW-05/07, BR-PUBLIC-01/02/03.
> - **BR working labels (srs-v3.md inline)**: BR codes referenced in TC files but sourced from master `srs-v3.md` Phụ lục B (BR-EC-01/03/04/12/13/19/20, BR-DATA-06...). Áp dụng FR-VII via inheritance — verify khi đọc master file.
> - **BR inline rule labels (BR-BM-*)**: Working labels gán cho inline rules trong SRS prose của srs-fr-09 (vd. BR-BM-03 = file format CHECK trong line 314). KHÔNG phải BR formal — dùng cho traceability nội bộ. Khi review coverage chính thức, chỉ tính BR formal §6.
> - Pragmatic: TC files dùng cả 3 loại BR labels. Coverage metric "BR ≥95%" áp dụng formal §6 only.

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực trước truy cập (2-tier) | srs-fr-09:877 | ✅ | Precondition login mọi UC |
| BR-AUTH-08 | Phân quyền theo đơn vị (don_vi_id) | srs-fr-09:883 | ✅ | TC permission scope |
| BR-DATA-01 | Soft delete (is_deleted=1) | srs-fr-09:889 | ✅ | TC DELETE |
| BR-DATA-03 | 7 common fields | srs-fr-09:895 | ✅ | Verify schema |
| BR-DATA-05 | Audit trail (immutable) | srs-fr-09:901 | ✅ | TC AUDIT_LOG |
| BR-DATA-07 | Pagination default 20, max 100 | srs-fr-09:907 | ✅ | TC pagination (TC-BM-211, TC-BM-509 — Codex 2026-05-09) |
| BR-FLOW-05 | Công khai qua API trực tiếp | srs-fr-09:913 | ✅ | TC publish Cổng PLQG |
| BR-FLOW-07 | BM công khai không cần PD | srs-fr-09:919 | ✅ (core) | TC công khai trực tiếp |
| BR-PUBLIC-01 | Điều kiện công khai BIEU_MAU: bất kỳ lúc nào | srs-fr-09:925 | ✅ (CR-01) | TC Switch ON |
| BR-PUBLIC-02 | Hủy công khai: cong_khai=0, clear thoi_gian_dang_tai | srs-fr-09:931 | ✅ (CR-01) | TC Switch OFF |
| BR-PUBLIC-03 | thoi_gian_dang_tai auto fill NOW() | srs-fr-09:937 | ✅ (CR-01) | TC verify timestamp |
| BR-EC-01 | Optimistic Locking | srs-v3.md | ✅ | TC conflict UPDATE |
| BR-EC-13 | Search sanitize max 200 ký tự | srs-v3.md | ✅ | TC search sanitize |
| BR-DATA-06 | Export Excel max 10,000 rows | srs-v3.md | ✅ | TC Export Excel |

### 2.2 Error Codes

**FR-VII-01 (THU_MUC):** ERR-TM-01 (trùng tên), ERR-TM-02 (có BM không xóa), ERR-TM-03 (>500 ký tự), ERR-TM-04 (lĩnh vực invalid)

**FR-VII-02 (Tìm kiếm TM):** ERR-TK-01 (tu_ngay > den_ngay), INF-TM-TK-01 (không kết quả)

**FR-VII-03 (Công khai TM):** ERR-CK-01 (TM rỗng), ERR-CK-02 (API Cổng lỗi), WRN-CK-01 (đã công khai)

**FR-VII-04 (BIEU_MAU):** ERR-BM-01 (file format), ERR-BM-02 (>20MB), ERR-BM-03 (tên trống), ERR-BM-04 (file corrupt), ERR-BM-05 (TM không tồn tại)

**FR-VII-06 (Import):** ERR-IMP-01 (all file lỗi), WRN-IMP-01 (partial lỗi), ERR-IMP-02 (>50 file), ERR-IMP-03 (>500MB)

### 2.3 Permission Matrix

| Entity / Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV/CG/DN |
|-----------------|------|------------------|-------------------|---------------|
| THU_MUC CRUD | 👁️ R | ✅ CRUD* (scope) | 👁️ R* (tìm kiếm) | ❌ |
| BIEU_MAU CRUD + upload | 👁️ R | ✅ CRUD* (scope) | 👁️ R* (tìm kiếm) | ❌ |
| Công khai (FR-VII-03) | ❌ | ✅ | ❌ | ❌ |
| Import (FR-VII-06) | ❌ | ✅ | ❌ | ❌ |

### 2.4 State Machine — SM-BIEUMAU

```
[*] → NHAP → CONG_KHAI ⟷ AN ; NHAP/AN → XOA
```

---

## 3. Cấu Trúc File Test Case

```
bieu-mau/
├── 00-test-plan-overview.md
├── 01-TC-quan-ly-thu-muc.md      ← FR-VII-01 UC92 (16 TC, A4 +4)
├── 02-TC-tim-kiem-thu-muc.md     ← FR-VII-02 UC93 (10 TC, A4 +3)
├── 03-TC-cong-khai-thu-muc.md    ← FR-VII-03 UC94 (9 TC, A4 +2)
├── 04-TC-quan-ly-bieu-mau.md     ← FR-VII-04 UC95 + CR-01 (22 TC, A6 +3, A4 +5, A7 -1)
├── 05-TC-tim-kiem-bieu-mau.md    ← FR-VII-05 UC96 (8 TC, A4 +2)
├── 06-TC-import-hang-loat.md     ← FR-VII-06 UC97 (11 TC, A4 +3)
├── 07-TC-permission-matrix.md    ← Permission cross-FR-VII (8 TC, A4 +2)
├── 08-REVIEW-edge-case-hunter.md ← A4 audit log (đã merge 21 TC vào 01-07)
├── 09-traceability-matrix.md     ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md     ← A6 6-axis quality score (86.7% PASS)
└── 11-a7-filter-log.md           ← A7 filter log (UC98 LOẠI, +3 A6 bổ sung)
```

> **Phase B B-block ref CHỈ 7 file UC (01-07)**, total 84 TC. File 08/09/10/11 là audit log không phải TC source.

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Tổng |
|------|------:|---------:|-----:|-----:|
| 01 - Thư mục CRUD | 6 | 4 | 7 | 17 |
| 02 - Tìm kiếm TM | 3 | 2 | 6 | 11 |
| 03 - Công khai TM | 4 | 3 | 2 | 9 |
| 04 - BM CRUD + CR-01 (incl. UI=1) | 10 | 9 | 6 | 25 |
| 05 - Tìm kiếm BM | 5 | 3 | 1 | 9 |
| 06 - Import hàng loạt (incl. UI=1) | 1 | 7 | 2 | 11 |
| 07 - Permission | 3 | 7 | 0 | 10 |
| **TỔNG (Phase A done · Codex review 2026-05-09)** | **32** | **35** | **24** | **92** |

> **Update 2026-05-06 (sau A4 inline merge):** 21 edge case từ file 08 đã merge inline vào 7 file UC (per plan.md §3.1 forced inline merge rule). File 08 chuyển thành audit log.
> *File 04 = 14 (A3 base) - 1 (A7 LOẠI TC-BM-413 UC98) + 3 (A6 bổ sung 401b/420/421) + 5 (A4 merge 415..419) = 21 + 1 UI = 22.*
> *File 06 includes 1 UI-verify TC (TC-BM-UI-06). File 04 includes 1 UI-verify TC (TC-BM-UI-04).*
> **Edge Case Review (08)**: ✅ MERGED 2026-05-06 — 4 P0 + 12 P1 + 5 P2 = 21 TC đã merge inline. File 08 = audit log only.
> **Traceability (09)**: BR 100% · AC 100% sau A6 · ERR 100% sau A6 · SM 100% · Permission 100%.
> **Test Quality Review (10)**: 86.7% PASS (≥80% threshold).
> **A7 Filter log (11)**: 100% UI/function-testable, 0 TC chỉ-DB/API thuần.
>
> **Update 2026-05-09 (Codex review):** +8 TC để fix coverage gap Codex flagged GATE: FAIL (5 P0 + 5 P1 + 2 P2):
> - TC-TM-027 (file 01): xem chi tiết TM srs-fr-09:141 — fix BM-CRIT-002.
> - TC-BM-211 (file 02): pagination boundary BR-DATA-07 — fix BM-HIGH-001.
> - TC-BM-422 + TC-BM-423 + TC-BM-424 (file 04): list BM/detail BM AC1-AC2 + SM-BIEUMAU 6 transitions trên entity BIEU_MAU — fix BM-CRIT-001 + BM-CRIT-003.
> - TC-BM-509 (file 05): search BM positive pagination AC1 — fix BM-HIGH-005.
> - TC-BM-PERM-009 + TC-BM-PERM-010 (file 07): CB_PD Import/Công khai block + NHT/TVV/CG block toàn module — fix BM-CRIT-005.
> - **Đã sửa:** TC-BM-305 (file 03 — bỏ BR-EC-20 fictitious, đổi sang SPEC-CLARIFY-BM-15 verify rollback policy thực tế), TC-BM-416 (file 04 — gắn SPEC-CLARIFY-BM-16), TC-BM-507 (file 05 — chuyển P1→P2, gắn SPEC-CLARIFY-BM-17), TC-BM-419 (file 04 — bỏ ref BR-EC-20 không tồn tại).
> - **Coverage sau Codex fix:** AC SRS 28/28 = 100% (was 24/28 = 85.7%); SM-BIEUMAU 6/6 transitions BIEU_MAU entity (was 2/6); Permission Matrix ~14/16 cells (was 8/16).
> - **SPEC-CLARIFY mới:** BM-15 (rollback ERR-CK-02), BM-16 (case-sensitivity .DOCX), BM-17 (search keyword scope mã BM), BM-18 (page_size=101 reject vs clamp), BM-19 (Switch OFF có set trang_thai=AN trên BIEU_MAU?).

---

## 5. Tiêu Chí Đạt / Không Đạt

- ✅ **PASS:** 100% P0 + 90% P1 pass
- ❌ **FAIL:** bất kỳ P0 FAIL hoặc P1 < 90%

---

## 6. SRS Gap pending BA sign-off

| # | Gap | Vị trí | Đề xuất |
|---|-----|--------|---------|
| G1 | thu_tu_hien_thi range 1-20 — behavior khi 2 TM cùng thứ tự? | srs-fr-09:91 | Flag BA |
| G2 | THU_MUC có `cong_khai` boolean + `trang_thai` — chồng ngữ nghĩa? | srs-fr-09:695,792 | Flag BA |
| G3 | BR-PUBLIC-01 BIEU_MAU luôn pass điều kiện CK? | srs-fr-09:319,925 | Flag BA |
| G4 | SM-BIEUMAU: NHAP→AN có transition hay chỉ CONG_KHAI→AN? | srs-fr-09:600,845 | Flag BA |
| G5 | sync_status PENDING mapping UI "Chờ"? | srs-fr-09:385,640 | Flag BA |
| G6 | file_dinh_kem_cong_khai thêm PDF nhưng file chính chỉ doc/docx/xls/xlsx | srs-fr-09:300,306 | Flag BA |
| G7 | SCR-VII-03 Excel metadata template columns? | srs-fr-09:663 | Flag BA |
| G8 (Codex 2026-05-09) | ERR-CK-02 rollback policy — transactional vs eventual consistency? | srs-fr-09:236,253 → SPEC-CLARIFY-BM-15 | Flag BA |
| G9 (Codex 2026-05-09) | File extension `.DOCX` UPPERCASE — BE case-sensitive vs case-insensitive? | srs-fr-09:300,314,344 → SPEC-CLARIFY-BM-16 | Flag BA |
| G10 (Codex 2026-05-09) | Search BM keyword có include mã BM hay chỉ tên/mô tả? | srs-fr-09:402,632 → SPEC-CLARIFY-BM-17 | Flag BA |
| G11 (Codex 2026-05-09) | Pagination page_size=101 — reject hay silent clamp về 100? | srs-fr-09:907 → SPEC-CLARIFY-BM-18 | Flag BA |
| G12 (Codex 2026-05-09) | BIEU_MAU.trang_thai (lifecycle) vs cong_khai (Switch CR-01) — Switch OFF có set trang_thai=AN không? | srs-fr-09:771,841-846 → SPEC-CLARIFY-BM-19 | Flag BA |

---

## 8. Phase A Checklist

- [x] A1 — Nghiên cứu SRS FR-09 (srs-fr-09-bieu-mau-v3.1.md)
- [x] A2 — Tạo 00-test-plan-overview.md
- [x] A3 — Sinh 7 file TC (01-07): 60 TC
- [x] A4 — Edge Case Hunter Review: +21 TC bổ sung (08-REVIEW)
- [x] A5 — Traceability: TraceID column mỗi TC → FR/BR/ERR
- [x] A6 — Quality Review: all ACs, error codes, BRs covered
- [x] A7 — UI Filter: FR-VII-07 (API thuần) LOẠI. 0 DB-only TC. All TC UI-executable.

**Phase A Status: ✅ HOÀN TẤT** (2026-05-06)
**Codex review patch: ✅ HOÀN TẤT** (2026-05-09)

---

*Generated 2026-05-06 — Phase A complete · Updated 2026-05-09 sau Codex review (5 P0 + 5 P1 + 2 P2 finding fixed; +8 TC; 84 → 92 TC).*
