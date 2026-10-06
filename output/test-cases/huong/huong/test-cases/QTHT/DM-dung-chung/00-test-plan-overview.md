# Kế Hoạch Kiểm Thử — DM Dùng Chung (FR-VIII-01..09, 11..13, 18, 19)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-08
> **Nguồn dữ liệu**: SRS v3.1 ([srs-fr-10-quan-tri-v3.1.md](../../../../input/srs-v3/srs-fr-10-quan-tri-v3.1.md) lines 56-880 + 1444-1496 + entity DON_VI/DANH_MUC §3.4.3.7-3.4.3.39, kèm [srs-v3.1.md](../../../../input/srs-v3/srs-v3.1.md) Phụ lục B cho BR cross-cutting)
> **SRS Reference**: FR-VIII-01..FR-VIII-09 (UC99-UC107), FR-VIII-11..FR-VIII-13 (UC109-UC111), FR-VIII-18 (UC116), FR-VIII-19 (UC117); Template TPL-DM-CRUD; Màn hình SCR-VIII-01 (MH-10.1) + tree view + cột bổ sung
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho module **DM Dùng Chung** — **13 DM trong scope** (SRS định nghĩa 14 FR-VIII-01..09 + 11..13 + 18..19, nhưng FR-VIII-06 UC104 Tổ chức tư vấn **đã chuyển sang Nhóm IV `[CR-02]`** — KHÔNG nằm trong scope W1.3). 13 DM = 9 chuẩn TPL + 1 tree 2-tầng (UC103) + 2 extended (UC109/110) + 1 đặc thù date/màu (UC101+UC102) — count 9+1+2+1=13 (với UC101/102 mỗi cái 1 DM riêng nên thực tế là **9 chuẩn + 4 đặc thù = 13 DM**).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử
- **13 FR DM trong scope** (SRS gốc 14, loại FR-VIII-06 CR-02) trên 1 màn hình (SCR-VIII-01 — MH-10.1) + UI variants:
  - Layout chuẩn: Danh sách + Modal CRUD + **13 sub-tab sidebar** (FR-VIII-06 ẩn theo CR-02)
  - Tree view 2-tầng cho UC103 Cơ quan ĐV (BR-AUTH-02)
  - Cột bổ sung cho UC109 (Trọng số/Thang điểm), UC110 (Quy mô/Mức/Trần)
- Entity chính: `DANH_MUC` (key-value, ~500 records, §3.4.3.39); `DON_VI` (cây 2-tầng, §3.4.3.7); audit qua `AUDIT_LOG`.
- Đặc thù v3.1:
  - **BR-AUTH-02 cây 2 tầng** (TW root → {BN, ĐP} ngang cấp song song dưới TW). FR-VIII-05 enforce — BN/DP đều có don_vi_cha_id trỏ TW; KHÔNG có quan hệ cha-con BN↔ĐP.
  - **FR-VIII-06 deprecate** chuyển sang Nhóm IV (FR-IV-NEW-01) — sidebar tab KHÔNG hiển thị Tổ chức tư vấn.
  - 13 sub-tab sidebar (theo SCR-VIII-01 line 1455).
- State Machine: KHÔNG áp dụng (DM không có vòng đời nghiệp vụ; chỉ Hoạt động/Vô hiệu hóa và Soft delete).
- Cross-cutting: Phân quyền dữ liệu BR-AUTH-08 (DANH_MUC ngoại lệ — NULL don_vi_id cho DM hệ thống); Audit log BR-DATA-05 cho mọi CUD.

### 1.2 Danh sách FR / UC

| # | Mã FR | UC | Tên DM | Đặc thù (vs TPL-DM-CRUD) | File Test Case |
|---|--------|-----|---------|---------------------------|----------------|
| 1 | FR-VIII-01 | UC99 | Lĩnh vực pháp lý | — (đại diện TPL chuẩn) | `01-TC-tpl-dm-CRUD-representative-LV-PL.md` (58 TC sau A4+A6) |
| 2 | FR-VIII-02 | UC100 | Loại hình hỗ trợ | — | `02-TC-smoke-11-dm-chuan.md` (smoke 5 TC) |
| 3 | FR-VIII-03 | UC101 | Chương trình HT | thoi_gian_bat_dau/ket_thuc + don_vi_chu_tri | `06-TC-chuong-trinh-ho-tro-date.md` (11 TC sau A4) |
| 4 | FR-VIII-04 | UC102 | Tình trạng vụ việc | thu_tu BẮT BUỘC + mau_hien_thi (HEX) | `07-TC-tinh-trang-vv-mau.md` (11 TC sau A4) |
| 5 | FR-VIII-05 | UC103 | Cơ quan đơn vị | **Tree 2-tầng (BR-AUTH-02)** + entity DON_VI riêng + cap TW/BN/DP | `03-TC-co-quan-don-vi-tree-2tier.md` (38 TC sau A4+R2) |
| 6 | FR-VIII-06 | UC104 | _(Tổ chức tư vấn — chuyển Nhóm IV CR-02, NOT IN SCOPE)_ | DEPRECATED W1.3 | _(không có file)_ |
| 7 | FR-VIII-07 | UC105 | Loại doanh nghiệp | tieu_chi_doanh_thu + tieu_chi_lao_dong (NĐ39/2018) | `08-TC-loai-dn-tieu-chi.md` (10 TC, prefix `TC-LDN-DEEP-XXX`) |
| 8 | FR-VIII-08 | UC106 | Hồ sơ đề nghị HT | thanh_phan_bat_buoc + thanh_phan_tuy_chon (structured JSON) | `09-TC-ho-so-thanh-phan.md` (16 TC sau A4, gộp UC106+107) |
| 9 | FR-VIII-09 | UC107 | Hồ sơ đề nghị TT | thanh_phan_ho_so (structured JSON) | _(gộp file 09)_ |
| 10 | FR-VIII-11 | UC109 | Tiêu chí ĐG hiệu quả | trong_so 0-100 + thang_diem min/max + **BR-CALC-04 tổng=100%** + WRN-TC-01 | `04-TC-tieu-chi-dg-hieu-qua.md` (24 TC sau A4+R2) |
| 11 | FR-VIII-12 | UC110 | Tiêu chí ĐG chi phí | quy_mo_dn (SIEU_NHO/NHO/VUA) + muc_ho_tro_phan_tram + tran_ho_tro_nam (NĐ18/2026) | `05-TC-tieu-chi-dg-chi-phi.md` (19 TC sau A4+R2) |
| 12 | FR-VIII-13 | UC111 | Loại tài khoản | — | `02-TC-smoke-11-dm-chuan.md` (5 TC trong file 02) |
| 13 | FR-VIII-18 | UC116 | Loại hình tiếp nhận | — | `02-TC-smoke-11-dm-chuan.md` (5 TC trong file 02) |
| 14 | FR-VIII-19 | UC117 | Kênh tiếp nhận | — | `02-TC-smoke-11-dm-chuan.md` (5 TC trong file 02) |
| — | All | — | Permission matrix | Cross-cutting BR-AUTH-01 + BR-AUTH-08 | `10-TC-permission-matrix.md` (16 TC) |

**Total Phase A active:** **255 TC** (56+55+38+24+19+11+11+10+16+15) sau A1-A7 + R1/R2/R3 Codex review fixes.
- A3 base: 228 TC (47+55+32+18+15+10+10+10+15+16)
- A4 edge inline: +18 TC → 246 TC
- A6 gap fill: +3 TC → 249 TC
- R2 Codex fill: +9 TC (UC103 ×3, UC109 ×4, UC110 ×2) → 258 TC declared
- R3 Codex LOẠI: −3 TC (TC-LV-036 case-insensitive, TC-LV-044 cross-module, TC-PERM-008 A7 fetch) → **255 TC active**
- R3 Codex REPHRASE: 7 TC chuyển từ assumption/DB direct → UI bridge + SPEC-CLARIFY (file 01: 4 TC; file 03: 2 TC; file 09: 1 TC)

**Strategy 187 trong plan §6.1 = floor**, actual **255 TC active** — vượt do user request cover sâu SRS + Codex full review (R1+R2+R3).

> **Tách file:** `02-TC-smoke-11-dm-chuan.md` gộp **11 DM smoke** (= 13 DM scope − 1 LV-PL deep ở file 01 − 1 UC103 ở file 03; còn 11 DM khác có 5 TC smoke mỗi DM × 11 = 55 TC; trong đó 4 DM UC101/102/109/110 có thêm file deep riêng (06/07/04/05) cho fields đặc thù — file 02 chỉ giữ shallow CRUD pattern). Lý do gộp: smoke chung pattern TPL-DM-CRUD, KHÔNG cần file riêng từng DM; vẫn tách rõ section per-DM trong file để dễ chạy partial.

> **TPL representative file 01:** Test 47 TC trên DM Lĩnh vực PL — coverage CRUD đầy đủ (List + Create + Update + Delete + Search + Pagination + Sort + Toggle trạng thái + Validation + Error + Boundary). Áp dụng kết quả cho 11 DM smoke = chỉ test các differences (Inputs riêng + Seed Data riêng + Ràng buộc xóa riêng).

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | qtht_01 | Primary CRUD toàn HT. `_02` fallback, `_03` permission test. |
| CB_NV_TW | TW | cb_nv_tw_01 | Negative — verify 403 cho mọi CUD DM (BR-AUTH-01: chỉ QTHT) |
| CB_NV_BN | BN | cb_nv_bn_01 | Negative — verify 403 |
| CB_NV_DP | DP | cb_nv_dp_01 | Negative — verify 403 |
| CB_PD_TW/BN/DP | — | cb_pd_tw_01 / cb_pd_bn_01 / cb_pd_dp_01 | Negative — verify 403 |
| NHT/TVV/CG/DN | — | nht_01, tvv_01, cg_01, dn_01 | Negative — verify 403 (Tier 2 KHÔNG vào CMS) |

> **Lý do:** SRS srs-fr-10:62 `Preconditions chung` nguyên văn "User có vai trò QTHT". TPL-DM-CRUD áp dụng BR-AUTH-01 ở mọi processing step. Nguời ngoài QTHT phải bị từ chối với ERR-AUTH-01.

> **READ-only DM:** Một số DM (Lĩnh vực PL, Loại hình HT, Cơ quan ĐV...) có thể được role khác READ qua dropdown trong các module khác (vd CB_NV chọn lĩnh vực khi tiếp nhận hỏi đáp). Nhưng **truy cập trực tiếp SCR-VIII-01 + CUD = chỉ QTHT**. Test READ qua module khác KHÔNG nằm trong scope W1.3 (sẽ test ở module dùng).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực + chỉ QTHT (Tier 1) | srs-fr-10:62, 82, 93, 104, 116; srs-v3.1 §B.1 | ✅ | Precondition mọi UC + permission matrix |
| BR-AUTH-02 | Cấu trúc 2 tầng TW → {BN, ĐP} ngang cấp song song. ĐP.don_vi_cha_id = TW.id (trực tiếp, KHÔNG qua BN) | srs-fr-10:319, 1967, 2161 | ✅ (UC103 only) | TC tree creation, validate guard cap-cha |
| BR-AUTH-03 | Ngang cấp KHÔNG thấy nhau (BN↔BN, ĐP↔ĐP, BN↔ĐP) | srs-fr-10:2167 | ✅ (UC103 read scope) | Test scope filter list đơn vị |
| BR-AUTH-04 | Cấp cha thấy cấp con — chỉ TW thấy toàn bộ | srs-fr-10:2173 | ✅ (UC103) | TW QTHT thấy 1 + 18 + 63; BN/DP cấp cha (nếu phân quyền data đặc biệt) |
| BR-AUTH-08 | Multi-tenant scoping cho mọi bảng có don_vi_id; **DANH_MUC ngoại lệ NULL** | srs-fr-10:2191; §3.4.3.39 ngoại lệ DM hệ thống | ✅ | Verify DM dùng chung KHÔNG bị scoped theo đơn vị khi list |
| BR-DATA-01 | Soft delete (is_deleted=1) | srs-fr-10:2203 | ✅ | TC delete → record vẫn tồn tại nhưng ẩn khỏi list |
| BR-DATA-02 | Multi-tenant don_vi_id NOT NULL — **ngoại lệ DM hệ thống NULL** | srs-fr-10:2209 | ✅ | DDL/seed-check (UI ẩn — verify qua list không có column don_vi_id) |
| BR-DATA-03 | 7 common fields (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | srs-fr-10:2215 | ✅ | Verify created_at/updated_at hiển thị format dd/mm/yyyy HH:mm |
| BR-DATA-05 | Audit trail mọi CUD — immutable | srs-fr-10:2221 | ✅ | Cross-ref AUDIT_LOG sau CRUD (qua module Nhật ký HT W1.1) |
| BR-DATA-06 | Export Excel max 10.000 rows | srs-v3.1.md §B.2.6 | ⚠️ partial (DM Cơ quan ĐV có nút Xuất Excel nếu có) | TC export DM (nếu UI hỗ trợ) |
| BR-DATA-07 | Pagination default 20, max 100 | srs-fr-10:85, 2227 | ✅ | TC pagination 20/page mặc định + 100/page max |
| BR-CALC-04 | Tổng trọng số tiêu chí ĐG = 100% (warning nếu khác) | srs-fr-10:541-543, 2257 | ✅ (UC109 only) | TC tổng != 100 → WRN-TC-01, vẫn cho lưu |
| BR-EC-13 | Search sanitize 200 ký tự + escape SQL/XSS | srs-v3.1.md §B.5.13 | ✅ | TC search keyword malicious (SQL/XSS) |

### 2.2 Error Codes / Messages

**TPL-DM-CRUD chung (srs-fr-10:147-156):**
- `ERR-AUTH-01` ERROR — "Bạn không có quyền thực hiện chức năng này" (E1)
- `ERR-AUTH-02` ERROR — Redirect `/login` (E2 session)
- `ERR-DM-01` ERROR — "Mã '{ma}' đã tồn tại trong danh mục {loai}" (E3 unique mã)
- `ERR-DM-02` ERROR — "Tên danh mục là bắt buộc" (E4)
- `ERR-DM-03` ERROR — "Không thể xóa. Danh mục đang được sử dụng bởi {N} bản ghi {entity}" (E5 ràng buộc xóa)
- `ERR-DM-04` ERROR — "Bản ghi không tồn tại hoặc đã bị xóa" (E6)
- `ERR-DM-05` ERROR — "Mã danh mục tối đa 20 ký tự" (E7)

**FR-VIII-05 Cơ quan ĐV (srs-fr-10:343-348):**
- `ERR-DV-01` ERROR — "Mã đơn vị '{ma}' đã tồn tại"
- `ERR-DV-02` ERROR — "Cấp {cap} phải có đơn vị cha"
- `ERR-DV-03` ERROR — "Không thể xóa. Đơn vị có {N} tài khoản liên kết"
- `ERR-DV-04` ERROR — "Không thể xóa. Đơn vị có {N} bản ghi dữ liệu"
- `ERR-DV-05` ERROR — "Không thể tạo vòng lặp phân cấp"

**FR-VIII-11 Tiêu chí ĐG hiệu quả (srs-fr-10:548-549):**
- `WRN-TC-01` WARNING — "Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100% trước khi sử dụng"
- `ERR-TC-01` ERROR — "Điểm tối thiểu phải nhỏ hơn điểm tối đa"

**Empty state (SCR-VIII-01):**
- "Không tìm thấy danh mục phù hợp." (assumed — SRS không nguyên văn, mark SPEC-CLARIFY-DM-01)

### 2.3 Permission Matrix

| Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV/CG/DN |
|--------|------|------------------|-------------------|---------------|
| Truy cập SCR-VIII-01 (CMS) | ✅ | ❌ ERR-AUTH-01 | ❌ ERR-AUTH-01 | ❌ (Tier 2 không CMS) |
| LIST 13 DM | ✅ | ❌ | ❌ | ❌ |
| CREATE / UPDATE / DELETE / TOGGLE | ✅ | ❌ | ❌ | ❌ |
| Cây Cơ quan ĐV (UC103) — toàn cây | ✅ TW thấy tất cả | ❌ direct CRUD | ❌ | ❌ |
| READ DM dropdown trong module khác (vd chọn lĩnh vực khi tiếp nhận HĐ) | ✅ | ✅ (READ scope role) | ✅ | scope DN/TVV — module gốc |

> **Iron rule:** TPL-DM-CRUD bước 1 mọi processing = "Kiểm tra quyền QTHT (BR-AUTH-01)". Nguời không QTHT vào URL `/quan-tri/danh-muc/...` → 403 ERR-AUTH-01. KHÔNG có "scope READ-only QTHT cấp BN/DP" — QTHT là single role TW level.

### 2.4 State Machine — N/A

Module DM không có state machine nghiệp vụ. Chỉ 2 trạng thái boolean:
- `trang_thai = 1` (Hoạt động/Kích hoạt) — mặc định
- `trang_thai = 0` (Không hoạt động/Vô hiệu hóa)

Plus `is_deleted = 1` (soft delete BR-DATA-01) — record ẩn khỏi list nhưng vẫn tồn tại DB.

UC103 DON_VI có 2 trạng thái: `HOAT_DONG` / `TAM_DUNG` (entity §3.4.3.7 line 1973).

### 2.5 Inputs Fields per UC

**TPL-DM-CRUD common (srs-fr-10:69-77):**
| # | Field | Type | Bắt buộc | Constraint |
|---|-------|------|----------|------------|
| 1 | ma | text | Y | Unique trong loại, max 20 ký tự |
| 2 | ten | text | Y | Không trống |
| 3 | mo_ta | text | N | — |
| 4 | thu_tu | number | N | — (default 0) — **UC102 có Y bắt buộc, vd ngoại lệ** |
| 5 | trang_thai | boolean | Y | Default 1 |

**Per-UC fields đặc thù (xem detail trong file TC riêng):**
- UC101 (CT HT): thoi_gian_bat_dau (Y), thoi_gian_ket_thuc (N), don_vi_chu_tri (Y)
- UC102 (TT VV): thu_tu (Y, **bắt buộc** vs N TPL), mau_hien_thi (N, HEX format)
- UC103 (CQ ĐV — entity DON_VI): ma_don_vi, ten_don_vi, cap (TW/BN/DP), don_vi_cha_id (Y khi BN/DP), dia_chi/dien_thoai/email
- UC105 (Loại DN): tieu_chi_doanh_thu, tieu_chi_lao_dong (text NĐ39/2018)
- UC106 (HSDN HT): thanh_phan_bat_buoc, thanh_phan_tuy_chon (structured JSON)
- UC107 (HSDN TT): thanh_phan_ho_so (structured JSON)
- UC109 (TC HQ): trong_so (Y, 0-100), thang_diem_min (Y), thang_diem_max (Y, > min)
- UC110 (TC CP): quy_mo_dn (Y, SIEU_NHO/NHO/VUA), muc_ho_tro_phan_tram (Y), tran_ho_tro_nam (Y, money)

### 2.6 Output Columns (SCR-VIII-01 #5-10)

| # | Cột | Format | Sortable? | Đặc thù |
|---|-----|--------|-----------|---------|
| 1 | Mã | text (max 20) | — | — |
| 2 | Tên | text | — | — |
| 3 | Mô tả | text (truncate) | — | — |
| 4 | Thứ tự | number | — | — |
| 5 | Trạng thái | toggle (Hoạt động/Không) | — | Click toggle → cập nhật ngay (inline) |
| 6 | Hành động | button (Sửa/Xóa) | — | `<a>` tag per CLAUDE.md selector library |

**UC109 thêm cột:** Trọng số (%), Thang điểm min, Thang điểm max + label "Tổng: {X}%" (xanh=100%, đỏ ≠100%)
**UC110 thêm cột:** Quy mô DN, Mức hỗ trợ (%), Trần hỗ trợ/năm (VNĐ)
**UC103 thay layout:** Cây đơn vị (tree-view bên trái) + Form chi tiết (panel bên phải) thay vì danh sách

---

## 3. Cấu Trúc File Test Case

```
output/test-cases/QTHT/DM-dung-chung/
├── 00-test-plan-overview.md                          ← FILE NÀY
├── 01-TC-tpl-dm-CRUD-representative-LV-PL.md         ← 56 TC active (58 declared − 2 LOẠI R3)
├── 02-TC-smoke-11-dm-chuan.md                        ← 55 TC (smoke 11 DM × 5)
├── 03-TC-co-quan-don-vi-tree-2tier.md                ← 38 TC (UC103 đặc thù tree, sau A4+R2)
├── 04-TC-tieu-chi-dg-hieu-qua.md                     ← 24 TC (UC109 trọng số 100% + thang điểm, sau A4+R2)
├── 05-TC-tieu-chi-dg-chi-phi.md                      ← 19 TC (UC110 quy mô/mức/trần, sau A4+R2)
├── 06-TC-chuong-trinh-ho-tro-date.md                 ← 11 TC (UC101 date range + don_vi_chu_tri, sau A4)
├── 07-TC-tinh-trang-vv-mau.md                        ← 11 TC (UC102 thu_tu Y + mau HEX, sau A4)
├── 08-TC-loai-dn-tieu-chi.md                         ← 10 TC (UC105 tiêu chí DT/LĐ, prefix TC-LDN-DEEP-XXX)
├── 09-TC-ho-so-thanh-phan.md                         ← 16 TC (UC106+UC107 JSON cấu trúc, sau A4)
├── 10-TC-permission-matrix.md                        ← 15 TC active (16 declared − 1 LOẠI R3 TC-PERM-008 A7)
├── 08-REVIEW-edge-case-hunter.md                     ← A4 audit log
├── 09-traceability-matrix.md                         ← A5 BR/AC ↔ TC
├── 10-REVIEW-test-quality.md                         ← A6 audit log
└── 11-a7-filter-log.md                               ← A7 UI/function filter log
```

> **Phase A → B handoff (lesson learned 2026-05-06 W2.3):** Phase B chỉ ref 10 file UC `01..10-TC-*.md`. File 08-REVIEW + 10-REVIEW + 11-a7-filter là **audit log** — KHÔNG phải TC source.

---

## 4. Strategy TPL-DM-CRUD Representative + Smoke

### 4.1 File 01 (47 TC TPL representative — DM Lĩnh vực PL)

Test toàn bộ TPL-DM-CRUD pattern. Coverage:
- **CRUD List (8 TC):** Render table, sort thu_tu/ten, pagination 20/100, filter trạng thái, empty state
- **CRUD Create (10 TC):** Happy path, validate ma unique, validate ten not null, validate ma 20 chars boundary, validate trang_thai default, audit log INSERT
- **CRUD Update (8 TC):** Happy path, validate ma unique exclude self, validate ten not null, audit log UPDATE old→new
- **CRUD Delete (6 TC):** Soft delete happy path, ràng buộc tham chiếu (linh_vuc_id ở HOI_DAP/VU_VIEC/TVV/CAU_HINH_PHAN_CONG/KHO_CAU_HOI), confirm modal
- **Search (5 TC):** Substring match ma + ten, case-insensitive, sanitize SQL/XSS BR-EC-13, max 200 chars
- **Toggle trạng thái (3 TC):** Enable→Disable, Disable→Enable, audit log
- **Permission (3 TC):** QTHT happy, CB_NV 403, session expired

### 4.2 File 02 (Smoke 11 DM × 5 TC = 55 TC)

11 DM smoke = 13 DM scope − file 01 LV-PL − file 03 UC103. Cho mỗi DM smoke 5 TC tối thiểu:
- TC-1: List + render đúng tab
- TC-2: Create happy path (với Inputs đặc thù DM)
- TC-3: Validate ma unique trong loại
- TC-4: Update + audit log
- TC-5: Delete (với ràng buộc tham chiếu DM riêng)

> **DM list trong file 02:** FR-VIII-02 (Loại hình HT), FR-VIII-07 (Loại DN — basic level chỉ 5 TC, đặc thù tieu_chi ở file 08), FR-VIII-08 (HSDN HT — basic 5 TC, JSON đặc thù ở file 09), FR-VIII-09 (HSDN TT — basic 5 TC, JSON đặc thù ở file 09), FR-VIII-13 (Loại TK), FR-VIII-18 (Loại hình TN), FR-VIII-19 (Kênh TN). 7 DM × 5 = 35 TC. Còn lại tăng từ A4 inline edge.

> **NOTE:** File 02 sẽ điều chỉnh sau A4. Mục tiêu: cover SRS, không cap số.

---

## 5. SPEC-CLARIFY (master list — 20 entries pending BA Phase B sau R4 cleanup)

| ID | Vấn đề | Nguồn SRS line | Câu hỏi BA | Source file |
|----|---------|---------------|------------|-------------|
| SPEC-CLARIFY-DM-01 | Empty state text exact | SCR-VIII-01 #11 (line 1462 thiếu) | Text empty state khi list rỗng? "Không tìm thấy" có chuẩn không? | 01 + 02 |
| SPEC-CLARIFY-DM-02 | FR-VIII-06 Tổ chức tư vấn deprecated UI | line 359-379 | Tab Tổ chức tư vấn có còn hiển thị trên SCR-VIII-01 không sau CR-02? | 00 |
| SPEC-CLARIFY-DM-04 | UC101 thoi_gian_ket_thuc < bat_dau guard | line 252 | Validate thoi_gian_ket_thuc >= thoi_gian_bat_dau? Spec không nguyên văn | 06 |
| SPEC-CLARIFY-DM-06 | UC109 thang_diem_max upper bound | line 534 | thang_diem_max có cap (vd 1000)? Spec chỉ nói > min | 04 |
| SPEC-CLARIFY-DM-08 | UC110 muc_ho_tro_phan_tram boundary | line 567 | Range 0-100? Có thể > 100 không? | 05 |
| SPEC-CLARIFY-DM-09 | UC110 tran_ho_tro_nam negative | line 568 | Validate >= 0? Spec im lặng | 05 |
| SPEC-CLARIFY-DM-11 | UC103 đổi cap TW→BN/DP của record có con | line 320 | Có guard "đơn vị cha có tham chiếu từ đơn vị con" trước khi đổi cap không? | 03 |
| SPEC-CLARIFY-DM-12 | UC106/107 cấu trúc thanh_phan format | line 416, 435 | "structured" type — JSON shape exact? Validate gì khi nhập? | 09 |
| SPEC-CLARIFY-DM-13 | Mã DM ký tự cho phép | line 72 | "max 20 ký tự" nhưng có cấm ký tự đặc biệt không (space, dấu, unicode)? | 01 |
| SPEC-CLARIFY-DM-18 | Xóa TW root có guard không? | line 343-348 | Spec không nói explicit về delete TW root — có block không? | 03 |
| SPEC-CLARIFY-DM-19 | UC105 max length text tieu_chi | line 395-396 | tieu_chi_doanh_thu/lao_dong text long — cap max length? | 08 |
| SPEC-CLARIFY-DM-20 | Whitespace handling ma + ten | line 71-72 | Backend trim leading/trailing? FE preserve? | 01 |
| SPEC-CLARIFY-DM-21 | Soft-deleted + re-create cùng ma | line 95, BR-DATA-01 | Re-create ma đã soft-delete có reuse hay reject? | 01 |
| SPEC-CLARIFY-DM-22 | UC103 đổi cap TW → BN/DP có children | line 1967 | Cascade rule khi đổi cap TW có 18 BN + 63 DP children? | 03 |
| SPEC-CLARIFY-DM-23 | UC103 trang_thai TAM_DUNG impact session | line 1973 | Đơn vị TAM_DUNG → TK đang session active có bị invalidate? | 03 |
| SPEC-CLARIFY-DM-24 | UC110 muc_ho_tro decimal | line 567 | muc_ho_tro_phan_tram int hay decimal? | 05 |
| SPEC-CLARIFY-DM-25 | UC101 snapshot pattern khi sửa thoi_gian | line 247-253 | CHUONG_TRINH_HTPL đang ACTIVE giữ thoi_gian cũ hay update? | 06 |
| SPEC-CLARIFY-DM-26 | UC106/107 thành phần item duplicate ten | line 416, 435 | Items cùng ten trong array có cho phép? | 09 |
| SPEC-CLARIFY-DM-28 | Concurrent edit resolution | line 100-110 | 2 user edit cùng record → last-write hay lock pessimistic? | 01 |
| SPEC-CLARIFY-DM-29 | Đổi cap đơn vị có TK liên kết | line 1478 | Data scope của 5 TK linked có cập nhật theo cấp mới sau alert phân quyền? | 03 |

> **R4 Cleanup log:** Loại 9 SPEC-CLARIFY (~31% reduction từ 29 → 20) sau Codex review verify SRS:
> - DM-03 (UC102 thu_tu Y) — line 277 nguyên văn rõ
> - DM-05 (trong_so range) — line 532 "0-100%" rõ
> - DM-07 (BR-CALC-04 cap upper) — line 542 chỉ WARNING, không cap
> - DM-10 (TW có cha form) — line 1967 NULL khi cap=TW rõ
> - DM-14 (pagination cap 100) — BR-DATA-07 line 2227 max 100 rõ
> - DM-15 (nút [+ Thêm con] BN/DP) — BR-AUTH-02 mô hình 2-tier rõ
> - DM-16 (cap=DP với cha=BN) — line 319 "cha phải = TW" rõ
> - DM-17 (Multi-TW) — BR-AUTH-02 1 TW root duy nhất rõ
> - DM-27 (Export Excel UI) — out-of-scope SCR-VIII-01 (BR-DATA-06 không expose ở DM)

---

## 6. Acceptance Criteria — Phase A done

- ✅ A1-A7 7 bước done
- ✅ Traceability ≥95% BR + 100% AC (kiểm chứng qua file 09)
- ✅ 0 TC chỉ-DB/API thuần (A7 verified, log ở file 11)
- ✅ 0 TC sống ở file phụ (08/10/11 chỉ là audit, mọi TC trong 01..10)
- ✅ SPEC-CLARIFY listed (**20 entries** sau R4 cleanup, gửi BA Phase B)
- ✅ Phase B handoff: 10 file UC `01..10-TC-*.md` ready, B-block chỉ ref 10 file này
