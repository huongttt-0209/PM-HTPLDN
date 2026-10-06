# Kế Hoạch Kiểm Thử — Hợp đồng Tư vấn (FR-14, Nhóm X.3, SCR-X3-01)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-10
> **Nguồn dữ liệu**: SRS v3.5 ([srs-fr-14-hop-dong-tv-v3.1.md](../../../input/srs-v3/srs-fr-14-hop-dong-tv-v3.1.md), kèm [srs-v3.md](../../../input/srs-v3/srs-v3.md) cho BR Phụ lục B, Phụ lục C)
> **Business flow ref**: [14-fr-14-hop-dong-tv.md](../../../input/bussiness/bussiness-flow/14-fr-14-hop-dong-tv.md)
> **Module thứ tự ref**: [02-thu-tu-module.md](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §⑩ FR-14
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho module Hợp đồng tư vấn pháp lý (HĐ TV). Chỉ CRUD thuần, **KHÔNG có vòng đời phê duyệt**. 4 trạng thái đơn giản (`DANG_THUC_HIEN`/`HOAN_THANH`/`HUY`/`TAM_DUNG`). Bao gồm 5 accordion (Thông tin chung / VV liên kết / Mốc tiến độ / Thanh toán giai đoạn / Nhật ký).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử
- 2 FR (UC159 + UC159e) trên 1 màn hình `SCR-X3-01` (List + Form Accordion).
- Entity chính: `HOP_DONG_TU_VAN` (owned). Referenced: `TU_VAN_VIEN`, `VU_VIEC`, `DOANH_NGHIEP`, `TAI_KHOAN`, `DON_VI`.
- Mốc tiến độ + Thanh toán giai đoạn lưu dạng JSON array trong cột entity HĐ.
- Liên kết VV: many-to-many (junction `HD_VV` theo business-flow §2; SRS chỉ ghi `vu_viec_ids[]` input).
- Embedded drawer/modal: truy cập từ chi tiết VV (SCR-V.I-03 → "HĐ tư vấn liên kết") + chi tiết TVV (SCR-IV-03 → tab "Lịch sử").
- 4 transition trạng thái HĐ (TODO UNVERIFIED — flag SPEC-CLARIFY).
- Đặc thù: **KHÔNG cần phê duyệt** (CRUD thuần). Xóa chặn nếu còn VV liên kết.

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|-------|----------|---------------|--------|----------------|
| 1 | FR-X.3-01 | UC159 | Quản lý HĐ tư vấn (CRUD + 4 accordion: Thông tin chung / VV liên kết / Mốc tiến độ / Thanh toán giai đoạn) + Xuất Excel | HOP_DONG_TU_VAN | `01-TC-quan-ly-hd-tv-CRUD.md` |
| 2 | FR-X.3-01 | UC159 | Mốc tiến độ (inline-edit) | HOP_DONG_TU_VAN.moc_tien_do | `02-TC-moc-tien-do.md` |
| 3 | FR-X.3-01 | UC159 | Thanh toán giai đoạn (inline-edit + ràng buộc Σ ≤ giá trị HĐ) | HOP_DONG_TU_VAN.thanh_toan_giai_doan | `03-TC-thanh-toan-giai-doan.md` |
| 4 | FR-X.3-01 | UC159 | Liên kết Vụ việc N:N (link / unlink) + Xóa chặn nếu có VV | HOP_DONG_TU_VAN ↔ VU_VIEC | `04-TC-lien-ket-vu-viec.md` |
| 5 | FR-X.3-02 | UC159e | Tìm kiếm HĐ (keyword + TVV + khoảng ngày) | HOP_DONG_TU_VAN | `05-TC-tim-kiem-hd-tv.md` |
| 6 | — | — | Permission matrix cross FR-14 | All | `06-TC-permission-matrix.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|----------------------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (toàn HT). KHÔNG được CRUD HĐ |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD primary (scope TW). `_02` fallback, `_03` permission test |
| CB_NV_BN | BN | cb_nv_bn_01 (Bộ KH&ĐT) | CRUD scoped BN |
| CB_NV_DP | DP | cb_nv_dp_01 (Sở TP AG) | CRUD scoped ĐP. `_02` Sở TP BG → cross-tenant test |
| CB_PD_TW | TW | cb_pd_tw_01 | Read-only (xem + tìm kiếm). KHÔNG CRUD (HĐ không có duyệt) |
| CB_PD_BN | BN | cb_pd_bn_01 | Read-only scoped BN |
| CB_PD_DP | DP | cb_pd_dp_01 | Read-only scoped ĐP |
| NHT/TVV/CG/DN/GV | — | nht_01, tvv_01, cg_01, dn_01 | Negative — verify 403 chặn module |

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực 2-tier | srs-fr-14:464,471-478 | ✅ | Precondition login mọi UC |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` (no exception cho HĐ) | srs-fr-14:465,480-487 | ✅ | TC permission scope cross-tenant |
| BR-DATA-01 | Soft delete (is_deleted=1) | srs-fr-14:466,489-496 | ✅ | TC DELETE HĐ (chỉ khi không có VV) |
| BR-DATA-04 | Sinh mã tự động `HDTV-YYYYMMDD-SEQ` | srs-fr-14:467,498-504 | ✅ | TC tạo HĐ mới |
| BR-DATA-05 | Audit trail immutable | srs-fr-14:468,506-512 | ✅ | TC verify Nhật ký |
| BR-DATA-07 | Pagination default 20, max 100 | srs-fr-14:469,514-520 | ✅ | TC tìm kiếm + danh sách |

### 2.2 Error Codes & Info Codes

**FR-X.3-01 (CRUD HĐ):**
- ERR-HDTV-01: Tên HĐ trống
- ERR-HDTV-02: Ngày bắt đầu > ngày kết thúc
- ERR-HDTV-03: Tổng thanh toán giai đoạn > giá trị HĐ
- ERR-HDTV-04: Xóa HĐ khi còn VV liên kết
- ERR-HDTV-05: Giá trị HĐ ≤ 0

**FR-X.3-02 (Tìm kiếm):**
- ERR-HDTV-TK-01: tu_ngay > den_ngay
- INF-HDTV-TK-01: Không có kết quả

### 2.3 Permission Matrix

| Entity / Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV/CG/DN/GV |
|-----------------|------|------------------|-------------------|---------------------|
| Xem danh sách HĐ | 👁️ R (OBS) | 👁️ R | 👁️ R | ❌ |
| CRUD HĐ (Tạo/Sửa/Xóa) | ❌ | ✅ (scope đơn vị) | ❌ | ❌ |
| Mốc tiến độ + Thanh toán + Liên kết VV | ❌ | ✅ (scope đơn vị) | ❌ | ❌ |
| Tìm kiếm (UC159e) | 👁️ R (OBS) | 👁️ R | 👁️ R | ❌ |
| Xuất Excel | ❌ | ✅ | ❌ (SRS §2 line 129 chỉ CB NV) | ❌ |

> **Codex P1-3 RESOLVED:** CB_PD KHÔNG có Excel — Processing Excel step 1 SRS line 129 quote "Kiểm tra quyền CB NV". Bỏ SPEC-CLARIFY-HDTV-01.
> **OBS QTHT:** SRS actor lines 67, 195 + BR-AUTH-08 (line 484) không grant rõ QTHT quyền module HĐ. Read-only verify HT là practice gstack, không phải spec — flag BA confirm.

### 2.4 Trạng thái HĐ — KHÔNG có State Machine (per SRS §5 line 450-452)

> **SRS §5 nguyên văn (line 450):** "Nhóm X.3 (Hợp đồng tư vấn) không có state machine. HĐ tư vấn chỉ CRUD thuần, KHÔNG có phê duyệt."
> **SRS §5 line 452:** "Trạng thái HĐ (`DANG_THUC_HIEN`, `HOAN_THANH`, `HUY`, `TAM_DUNG`) chỉ là **status field đơn giản, không theo vòng đời phê duyệt**."

→ KHÔNG test SM transition như flow nghiệp vụ. Chỉ test field `trang_thai` như enum field thông thường (free-edit trong form, validate enum value). 02-thu-tu-module:643-653 quote "Transition (TODO UNVERIFIED) — suy luận từ enum + action bar, **cần CĐT clarify**" → không phải spec chính thức.

→ **SM coverage KHÔNG nằm trong gate Phase A.** Bỏ axis SM khỏi traceability matrix coverage threshold.

### 2.5 Field constraints (Inputs FR-X.3-01)

| Field | Bắt buộc | Kiểu | Ràng buộc |
|-------|----------|------|-----------|
| ma_hop_dong | Y (auto) | text | Format `HDTV-YYYYMMDD-SEQ` (BR-DATA-04) |
| ten_hop_dong | Y | text | Không trống (E1) |
| ben_a | Y (auto) | text | Hệ thống tự điền từ `don_vi_id` của user login |
| ben_b | Y | text | Nhập tay (TVV/Tổ chức tư vấn/Chuyên gia) |
| tvv_id | N | identifier | FK → TU_VAN_VIEN (loai_tvv = 'TVV' hoặc 'CG'); lọc `trang_thai=HOAT_DONG` |
| gia_tri_hop_dong | Y | money | > 0 (E5) |
| thoi_han_bat_dau | Y | date | — |
| thoi_han_ket_thuc | Y | date | ≥ thoi_han_bat_dau (E2) |
| noi_dung | N | text long | — |
| vu_viec_ids[] | N | identifier[] | FK[] → VU_VIEC (M2M) |
| ghi_chu | N | text long | — |
| file_dinh_kem[] | N | file[] | Upload nhiều file (định dạng + dung lượng SPEC-CLARIFY) |

**Mốc tiến độ:** ten_moc(Y), ngay_du_kien(Y), ngay_thuc_te(N), trang_thai_moc(Y) ∈ {CHUA_BAT_DAU, DANG_THUC_HIEN, HOAN_THANH}

**Thanh toán giai đoạn:** giai_doan(Y), so_tien(Y), ngay_thanh_toan(N), trang_thai_tt(Y) ∈ {CHUA_THANH_TOAN, DA_THANH_TOAN}; **Σ so_tien ≤ gia_tri_hop_dong** (E3).

---

## 3. Cấu Trúc File Test Case

```
hop-dong-tv/
├── 00-test-plan-overview.md
├── 01-TC-quan-ly-hd-tv-CRUD.md       ← FR-X.3-01 UC159 — Thông tin chung CRUD + Excel
├── 02-TC-moc-tien-do.md               ← FR-X.3-01 UC159 — Accordion Mốc tiến độ
├── 03-TC-thanh-toan-giai-doan.md      ← FR-X.3-01 UC159 — Accordion Thanh toán + Σ≤GT
├── 04-TC-lien-ket-vu-viec.md          ← FR-X.3-01 UC159 — VV M2M + xóa chặn
├── 05-TC-tim-kiem-hd-tv.md            ← FR-X.3-02 UC159e — Search + filter
├── 06-TC-permission-matrix.md         ← Cross FR-14 permission
├── 07-REVIEW-edge-case-hunter.md      ← A4 audit log
├── 08-traceability-matrix.md          ← A5 BR/AC ↔ TC matrix
├── 09-REVIEW-test-quality.md          ← A6 6-axis quality score
└── 10-a7-filter-log.md                ← A7 filter log
```

> **Phase B B-block ref CHỈ 6 file UC (01-06)**. File 07/08/09/10 là audit log.

---

## 4. Tổng Quan Số Lượng Test Cases (sau A1-A7 + Codex)

| File | Happy | Negative | Edge | Tổng |
|------|------:|---------:|-----:|-----:|
| 01 - HĐ CRUD + Excel + status field | 6 | 5 | 15 | 26 |
| 02 - Mốc tiến độ | 3 | 2 | 4 | 9 |
| 03 - Thanh toán giai đoạn (Σ≤GT) | 3 | 3 | 5 | 11 |
| 04 - Liên kết VV M2M | 3 | 2 | 6 | 11 |
| 05 - Tìm kiếm | 3 | 2 | 7 | 12 |
| 06 - Permission | 3 | 6 | 7 | 16 |
| **TỔNG (A1-A7 + Codex)** | **21** | **20** | **44** | **85** |

> A3 base: 54 TC · A4 +21 edge inline · A6 +5 fill status field/entity · A7 0 LOẠI · Codex +5 (TC-HDTV-029 Excel filter + TC-PERM-023..026 permission gaps).

---

## 5. Tiêu Chí Đạt / Không Đạt

- ✅ **PASS**: 100% P0 + 90% P1 pass
- ❌ **FAIL**: bất kỳ P0 FAIL hoặc P1 < 90%

---

## 6. SRS Gap pending BA sign-off (sau Codex review)

| # | Gap | Vị trí | Đề xuất | Status |
|---|-----|--------|---------|--------|
| HDTV-01 | ~~CB_PD có Xuất Excel HĐ không?~~ | srs-fr-14:129 | RESOLVED Codex P1-3: SRS line 129 quote "Kiểm tra quyền CB NV" → CB_PD = NO | ✅ RESOLVED |
| HDTV-02 | ~~SM-HOPDONG transition flow?~~ | srs-fr-14:450-452 | RESOLVED Codex P0-1: SRS §5 nói rõ "không có SM, chỉ status field". TC đã đổi sang field free-edit test. Action-bar = OBS chờ CĐT | ✅ RESOLVED (chỉ OBS action-bar) |
| HDTV-03 | `[GAP-X.3-02]` Excel template columns chính thức? | srs-fr-14:132,179 | Flag BA — quote SRS gap tag | ⏳ Pending BA |
| HDTV-04 | `[GAP-X.3-03]` AC tìm kiếm theo TVV / khoảng ngày — chính thức confirm field nào (`thoi_han_bat_dau`/`ngay_ky`/`created_at`)? | srs-fr-14:246-248 | Flag BA — quote SRS gap tag (Codex P2-4) | ⏳ Pending BA |
| HDTV-05 | file_dinh_kem định dạng + dung lượng + số lượng max? | srs-fr-14:90 | Flag BA — SRS silent (Codex P2-2 OBS) | ⏳ Pending BA |
| HDTV-06 | Mốc tiến độ + Thanh toán JSON array — UI có sort/edit/delete row riêng? | srs-fr-14:382-383 + business-flow §2 | Flag BA | ⏳ Pending BA |
| HDTV-07 | Liên kết VV M2M — bỏ liên kết (unlink) có audit log riêng? | business-flow §3 (G4) | Flag BA | ⏳ Pending BA |
| HDTV-08 | "Thời hạn kết thúc đỏ ≤30 ngày" — countdown realtime hay snapshot? | srs-fr-14:276 | Flag BA | ⏳ Pending BA |
| HDTV-09 | Dropdown TVV filter `loai_tvv` + `trang_thai`? | srs-fr-14:180 + 02-thu-tu-module:649 | Flag BA — TVV trạng_thái = HOAT_DONG (đã sửa P0-2) | ⏳ Pending BA |
| HDTV-10 | TVV trạng thái CHO_PHE_DUYET có loại trừ trong dropdown? | srs-fr-04 SM-TVV | Flag BA | ⏳ Pending BA |
| HDTV-11 | Collation tiếng Việt cho keyword search (có dấu vs không dấu)? | srs-fr-14:216 | Flag BA | ⏳ Pending BA |
| HDTV-12 | VV soft-delete có cascade hide khỏi accordion HĐ hay vẫn show? | BR-DATA-01 + N:N | Flag BA — TC-LVV-022 expected mặc định hide (Codex P2-5 OBS) | ⏳ Pending BA |
| HDTV-13 | Scope đơn vị áp lên list HĐ trong accordion VV cross-FR? | BR-AUTH-08 + N:N | Flag BA | ⏳ Pending BA |
| HDTV-14 | ghi_chu / noi_dung max length? | srs-fr-14:89 | Flag BA — SRS silent | ⏳ Pending BA |
| HDTV-15 (Codex P2-3) | so_tien giai đoạn `> 0` — SRS không có ERR riêng (chỉ ERR-HDTV-05 cho gia_tri_hop_dong) | srs-fr-14:106-110, 166-170 | Flag BA — bổ sung ERR riêng cho so_tien? | ⏳ Pending BA |
| HDTV-16 (Codex P2-1 OBS) | QTHT có quyền Read HĐ không? SRS không grant rõ | srs-fr-14:67,195,484 | Flag BA — practice OBS, không gate Phase A | ⏳ Pending BA |
| HDTV-17 (Codex P1-4 OBS) | Entity field `so_hop_dong` + `ngay_ky` (HOP_DONG_TU_VAN line 373, 378) — UI input chính thức chưa? | srs-fr-14:373,378 | Excluded từ SCR-X3-01 row#6 (Form không có 2 field này) — log OBS | ⏳ OBS Excluded |
| HDTV-18 (Codex P1-5 OBS) | CHECK constraint `moc_tien_do IS JSON` + `thanh_toan_giai_doan IS JSON` (line 388-389) | srs-fr-14:388-389 | Excluded A7 — DB-level constraint, không UI testable | ⏳ OBS Excluded |

---

## 7. Phase A Checklist

- [x] A1 — Đọc SRS FR-14 + business flow + sibling check
- [x] A2 — Tạo 00-test-plan-overview.md
- [x] A3 — Sinh 6 file TC (01-06): 54 TC
- [x] A4 — Edge Case Hunter Review: +21 TC inline merge (file 07)
- [x] A5 — Traceability matrix (file 08): BR 100% / AC 100% / ERR 100% / Permission 91.7% / Entity 91.7% (SM removed sau Codex P0-1)
- [x] A6 — Quality Review (file 09): +5 TC fill status field + entity. Quality 90.8% PASS
- [x] A7 — UI Filter (file 10): 0 LOẠI / 0 REWRITE / 80 GIỮ
- [x] **Codex review + apply patches**: GATE FAIL → fix 2 P0 + 5 P1 + 5 P2. **+5 TC** (TC-HDTV-029 + TC-PERM-023..026). Sửa data DANG_HOAT_DONG → HOAT_DONG. Sửa 4 TC SM transition → status field free-edit. Resolve SPEC-CLARIFY-HDTV-01/02. Add OBS HDTV-15..18.

**Phase A Status: ✅ HOÀN TẤT** (2026-05-10) — 85 TC final.

---

*Generated 2026-05-10 — Phase A step A2*
