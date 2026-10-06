# Kế Hoạch Kiểm Thử — Cấu hình Hệ thống (SCR-VIII-06 + FR-VIII-29)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-08
> **Nguồn dữ liệu**: SRS v3.1
>   - [`srs-fr-10-quan-tri-v3.1.md`](../../../../input/srs-v3/srs-fr-10-quan-tri-v3.1.md): FR-VIII-10 SLA (line 440-516), FR-VIII-29 Ngày lễ (line 1376-1434), SCR-VIII-06 4 tab (line 1609-1697)
>   - [`srs-fr-02-hoi-dap-v3.1.md`](../../../../input/srs-v3/srs-fr-02-hoi-dap-v3.1.md): FR-II-NEW-02 Mẫu phản hồi (line 891-967), FR-II-NEW-01 ĐÃ BỎ (line 885-887)
>   - [`srs-v3.1.md`](../../../../input/srs-v3/srs-v3.1.md): BR Phụ lục B + permission matrix §3.4.2 MAU_PHAN_HOI
>
> **SRS Reference**: SCR-VIII-06 (MH-10.7) gộp 4 Tab + FR-VIII-29 màn hình riêng
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho 5 sub-module:
>   - **Tab 1 — SLA** (FR-VIII-10) — chỉ QTHT
>   - **Tab 2 — Phân công mặc định** ⚠️ FR-II-NEW-01 ĐÃ BỎ (BA chốt 2026-05-07 Q11) → minimal TC verify deprecation
>   - **Tab 3 — Mẫu phản hồi** (FR-II-NEW-02) — Mô hình B Hybrid 2 tầng (TW/BN/DP scope) — phức tạp nhất
>   - **Tab 4 — Quy trình hỗ trợ** — placeholder cho cấu hình quy trình HTPL, snapshot cho hồ sơ đang xử lý
>   - **Ngày lễ** (FR-VIII-29) — màn hình danh mục con riêng

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử
- 1 màn hình tab gating (SCR-VIII-06) + 1 màn hình danh mục (FR-VIII-29).
- 4 Tab + 1 màn hình riêng = 5 sub-module functional.
- Entity: `CAU_HINH_SLA` (owned), `MAU_PHAN_HOI` (owned), `NGAY_LE` (owned), `CAU_HINH_PHAN_CONG` (DEPRECATED — entity đã bỏ), `CAU_HINH_QUY_TRINH_VV` (snapshot pattern).
- Đặc thù v3.1:
  - **Tab gating** theo role: QTHT thấy 4 tab; CB_NV chỉ thấy Tab 3; CB_PD chỉ thấy Tab 3 read-only.
  - **Mô hình B Hybrid 2 tầng** Tab 3: TW soạn mẫu khung quốc gia → 63 ĐP đọc; BN/ĐP có kho riêng (CĐT chốt 2026-05-02).
  - **Snapshot pattern** Tab 1 + Tab 4: HS đang xử lý giữ deadline cũ; HS mới áp config mới.
  - **FR-VIII-29 Ngày lễ** v3.1 mới — CRUD + Import Excel + Calendar view + tích hợp BR-CALC-03.
  - **FR-II-NEW-01 ĐÃ BỎ** (2026-05-07 Q11) — Tab 2 không còn functional; SCR-VIII-06 line 1647-1653 chưa update theo BA → SPEC-CLARIFY.

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-VIII-10 | UC108 | Cấu hình SLA (Tab 1) | CAU_HINH_SLA | `01-TC-tab-sla.md` (27 TC, P1 fixes 2026-05-08 codex) |
| 2 | FR-II-NEW-01 ⚠️ BỎ | — | Tab 2 Phân công — verify deprecated | (CAU_HINH_PHAN_CONG bỏ) | `02-TC-tab-phan-cong-deprecated.md` (3 TC) |
| 3 | FR-II-NEW-02 | UC mới | Tab 3 Mẫu phản hồi (Mô hình B Hybrid) | MAU_PHAN_HOI | `03-TC-tab-mau-phan-hoi.md` (42 TC — codex +1 BN dropdown CAUHINH-10) |
| 4 | (placeholder) | — | Tab 4 Quy trình hỗ trợ — snapshot config | CAU_HINH_QUY_TRINH_VV | `04-TC-tab-quy-trinh-ho-tro.md` (12 TC) |
| 5 | FR-VIII-29 | — | Quản lý ngày lễ | NGAY_LE | `05-TC-ngay-le.md` (22 TC, count fixed codex 23→22) |
| 6 | — | — | Permission matrix tab gating + role isolation | All | `06-TC-permission-matrix.md` (19 TC, PERM-001 fixed) |

**Total: 125 TC active** (sau codex review 2026-05-08: +1 net TC; 4 P1 fixes + 2 NEW SPEC-CLARIFY business-vs-business)

> **Note Tab 2:** SCR-VIII-06 line 1647-1653 vẫn render Tab 2 trong UI spec, nhưng srs-fr-02 line 885-887 + srs-fr-10 Lịch sử thay đổi 2026-05-07 Q11 đã bỏ FR-II-NEW-01 + entity CAU_HINH_PHAN_CONG. SPEC-CLARIFY-CAUHINH-01 cần BA chốt: Tab 2 ẨN hoàn toàn HAY render với deprecation banner?

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | qtht_01 | Tab 1+2+4 CRUD primary, Tab 3 READ-only, Ngày lễ CRUD. `_02` fallback, `_03` permission test |
| CB_NV_TW | TW | cb_nv_tw_01 | Tab 3 CRUD mẫu `pham_vi=TW_QUOC_GIA` + READ toàn quốc. `_02` fallback. |
| CB_NV_BN | BN | cb_nv_bn_01 (Bộ Tài chính), cb_nv_bn_02 (Bộ KH&ĐT) | Tab 3 CRUD mẫu `pham_vi=BN_RIENG` BN mình + READ mẫu TW. Cross-BN isolation test. |
| CB_NV_DP | DP | cb_nv_dp_01 (Sở TP HN), cb_nv_dp_02 (Sở TP HCM) | Tab 3 CRUD mẫu `pham_vi=DP_RIENG` ĐP mình + READ mẫu TW. Cross-ĐP isolation test. |
| CB_PD_TW/BN/DP | — | cb_pd_tw_01, cb_pd_bn_01, cb_pd_dp_01 | Tab 3 READ-only theo scope cấp; Tab 1/2/4 KHÔNG truy cập. |
| NHT/TVV/CG/DN | — | nht_01, tvv_01, cg_01, dn_01 | Negative — verify 403 cho toàn bộ SCR-VIII-06 + Ngày lễ |

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | Sub-module áp dụng |
|----|---------|-----------|----------|---------------------|
| BR-AUTH-01 | Authentication + role-based | srs-v3.1.md §B.1 | ✅ | Mọi sub-module — precondition |
| BR-AUTH-08 | Phân quyền theo đơn vị (ngoại lệ Mô hình B cho MAU_PHAN_HOI) | srs-v3.1.md §B.1 | ✅ | Tab 3 — exception: CB_NV cross-don_vi đọc được mẫu TW_QUOC_GIA |
| BR-DATA-01 | Soft delete (is_deleted=1) | srs-v3.1.md §B.2 | ✅ | Tab 3 mẫu, Ngày lễ DELETE |
| BR-DATA-03 | 7 common fields | srs-v3.1.md §B.2 | ✅ | Tab 3 mẫu CREATE, Ngày lễ CREATE |
| BR-DATA-05 | Audit log immutable | srs-v3.1.md §B.2 | ✅ | Mọi CUD action |
| BR-DATA-06 | Export Excel max 10K rows | srs-v3.1.md §B.2 | ⚠️ partial | Ngày lễ Import (đảo chiều) — KHÔNG export ở Tab 3 |
| BR-DATA-07 | Pagination default 20, max 100 | srs-v3.1.md §B.2 | ✅ | Tab 3 (20/page xác nhận line 1662) |
| BR-EC-01 | Optimistic Locking | srs-v3.1.md §B.4 | ✅ | Tab 1 + Tab 3 + Tab 4 (concurrent edit) |
| BR-EC-13 | Search sanitize max 200 + escape SQL/XSS | srs-v3.1.md §B.4 | ✅ | Tab 3 search box `ten_mau` |
| BR-SLA-01 | SLA mặc định 10 ngày LV (NĐ55) | srs-v3.1.md §B.5 | ✅ | Tab 1 verify default config |
| BR-SLA-02 | 4 mức cảnh báo (Bình thường/Sắp hết hạn/Quá hạn/Quá hạn nghiêm trọng) | srs-v3.1.md §B.5 | ✅ | Tab 1 |
| BR-SLA-04 | Ngày làm việc trừ ngày lễ | srs-v3.1.md §B.5 | ✅ | Ngày lễ → BR-CALC-03 |
| BR-CALC-03 | Deadline tính theo ngày làm việc, dùng entity NGAY_LE | srs-v3.1.md §B.5 | ✅ | Ngày lễ ↔ SLA integration |
| **Mô hình B Hybrid** | TW soạn mẫu khung 63 ĐP đọc; BN/ĐP kho riêng. MPH_CREATE_TW/BN/DP + MPH_READ scope | srs-v3.md §3.4.2; srs-fr-02:899; srs-fr-10:1617 | ✅ (đặc thù) | Tab 3 |
| **Snapshot pattern** | HS đang xử lý giữ config cũ; chỉ HS mới áp config mới | srs-fr-10:493; srs-fr-10:1645, 1675 | ✅ | Tab 1 + Tab 4 |

### 2.2 Error Codes / Messages

**Tab 1 SLA (FR-VIII-10):**
- `ERR-SLA-01` ERROR — "Thời hạn xử lý phải là số nguyên dương"
- `ERR-SLA-02` ERROR — "Mức cảnh báo 1 phải nhỏ hơn mức cảnh báo 2"
- `ERR-SLA-03` ERROR — "Loại yêu cầu đã có cấu hình SLA"

**Tab 3 Mẫu phản hồi (FR-II-NEW-02):**
- `ERR-MPH-01` ERROR — "Tên mẫu là bắt buộc"
- `ERR-MPH-02` ERROR — "Nội dung mẫu là bắt buộc"
- `ERR-MPH-03` ERROR — "Lĩnh vực pháp luật không hợp lệ"
- `ERR-MPH-04` ERROR (403) — "Bạn không có quyền tạo mẫu khung quốc gia. Chỉ Cán bộ Nghiệp vụ Trung ương được phép"
- `ERR-MPH-05` ERROR — "Phạm vi áp dụng không thể thay đổi sau khi tạo"
- `ERR-MPH-06` ERROR (403) — "Bạn chỉ được sửa/xóa mẫu thuộc đơn vị mình"

**Ngày lễ (FR-VIII-29):**
- `ERR-NL-01` ERROR — "Bạn không có quyền quản lý ngày lễ"
- `ERR-NL-02` ERROR — "Ngày kết thúc phải >= ngày bắt đầu"
- `ERR-NL-03` WARNING — "Khoảng thời gian trùng với ngày lễ '{ten}'"

### 2.3 Permission Matrix (action-level)

| Sub-module / Action | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_{cap} | NHT/TVV/CG/DN |
|---------------------|------|---------|---------|---------|-------------|---------------|
| **Tab 1 SLA** | ✅ CRUD | ❌ tab ẩn | ❌ | ❌ | ❌ | ❌ |
| **Tab 2 Phân công** ⚠️ | ✅ READ (deprecated) | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Tab 3 Mẫu PH — CREATE TW_QUOC_GIA** | ❌ | ✅ | ❌ ERR-MPH-04 | ❌ ERR-MPH-04 | ❌ | ❌ |
| **Tab 3 Mẫu PH — CREATE BN_RIENG** | ❌ | ❌ | ✅ (BN mình) | ❌ | ❌ | ❌ |
| **Tab 3 Mẫu PH — CREATE DP_RIENG** | ❌ | ❌ | ❌ | ✅ (ĐP mình) | ❌ | ❌ |
| **Tab 3 Mẫu PH — READ** | ✅ toàn quốc | ✅ toàn quốc | ✅ TW + BN mình | ✅ TW + ĐP mình | ✅ scope cấp | ❌ |
| **Tab 3 Mẫu PH — UPDATE/DELETE** | ❌ | ✅ TW của mình | ✅ BN của mình | ✅ ĐP của mình | ❌ | ❌ |
| **Tab 4 Quy trình** | ✅ CRUD | ❌ tab ẩn | ❌ | ❌ | ❌ | ❌ |
| **Ngày lễ FR-VIII-29** | ✅ CRUD | ❌ | ❌ | ❌ | ❌ | ❌ |

### 2.4 State Machine — N/A

Module config không có SM phức tạp. Có 1 trạng thái chuyển đổi nhỏ:
- **MAU_PHAN_HOI.trang_thai:** `KICH_HOAT ⟷ VO_HIEU_HOA` (toggle)
- **NGAY_LE:** soft delete `is_deleted=0/1`, không có lifecycle khác

### 2.5 Snapshot Pattern (Tab 1 + Tab 4 — đặc thù v3.1)

> **Iron rule:** Khi sửa SLA hoặc Quy trình, hồ sơ ĐANG XỬ LÝ vẫn giữ config snapshot cũ. CHỈ hồ sơ TẠO MỚI sau thời điểm save mới áp config mới.

**Test cụ thể:**
- Seed HS state DANG_XU_LY trước khi sửa SLA → verify deadline KHÔNG đổi sau save.
- Seed HS state TIEP_NHAN sau khi sửa SLA → verify deadline áp config mới.
- Verify alert UI nguyên văn (line 1645, 1675).

---

## 3. Cấu Trúc File Test Case

```
QTHT/Cau-hinh-he-thong/
├── 00-test-plan-overview.md         ← file này (A2)
├── 01-TC-tab-sla.md                 ← Tab 1 — FR-VIII-10 (CRUD inline + boundary CB1<CB2<100 + snapshot)
├── 02-TC-tab-phan-cong-deprecated.md ← Tab 2 — verify FR-II-NEW-01 deprecated (minimal)
├── 03-TC-tab-mau-phan-hoi.md        ← Tab 3 — FR-II-NEW-02 Mô hình B Hybrid (CRUD + cross-cấp scope + sanitize XSS)
├── 04-TC-tab-quy-trinh-ho-tro.md    ← Tab 4 — Quy trình HTPL (CRUD bước + snapshot HS đang xử lý)
├── 05-TC-ngay-le.md                 ← FR-VIII-29 (CRUD + Import Excel + Calendar + integration BR-CALC-03)
├── 06-TC-permission-matrix.md       ← Cross-tab gating + role isolation (BR-AUTH-01/08 + Mô hình B exception)
├── 08-REVIEW-edge-case-hunter.md    ← A4 audit log
├── 09-traceability-matrix.md        ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md        ← A6 6-axis quality score
└── 11-a7-filter-log.md              ← A7 filter log
```

> **Phase B B-block ref CHỈ 6 file UC (01-06)**. File 08/09/10/11 là audit log, KHÔNG phải TC source.

---

## 4. Coverage Target

| Loại | Target | Note |
|------|--------|------|
| BR coverage | ≥95% | 14 BR áp dụng (BR-AUTH-01/08, BR-DATA-01/03/05/06/07, BR-EC-01/13, BR-SLA-01/02/04, BR-CALC-03, Mô hình B, Snapshot) |
| AC coverage | 100% | 3 AC SLA + 7 AC Mẫu PH + 3 AC Ngày lễ = 13 AC |
| Error code coverage | 100% | 12 error codes (3 SLA + 6 MPH + 3 NL) |
| SM transition coverage | 100% | 1 transition `KICH_HOAT ⟷ VO_HIEU_HOA` (Tab 3) |
| Permission combo | 100% | 9 cells × {QTHT, CB_NV_{cap}, CB_PD_{cap}, Tier 2} |

---

## 5. Open Items / SPEC-CLARIFY

| ID | Status | Mô tả | SRS line | Action |
|----|--------|-------|----------|--------|
| ~~SPEC-CLARIFY-CAUHINH-01~~ | ✅ RESOLVED 2026-05-08 (theo business — FR-II-NEW-01 BỎ) | Tab 2 expected = ẨN HOẶC deprecation banner. UI spec line 1647-1653 chưa update theo BA Q11 → ignore. | srs-fr-02:885 ✓ vs srs-fr-10:1647 ✗ | TC-CH-PC-001: behavior (a)/(b) PASS, (c) render bảng CRUD = BUG. |
| SPEC-CLARIFY-CAUHINH-02 | ⏳ pending BA | SCR ghi FR-VIII-25 (VNeID) cho Tab 4 — sai ref, business spec chưa chỉ FR đúng. Đây là gap, không phải UI vs business pure conflict. | srs-fr-10:1612 vs 1671-1676 | Test theo SCR component spec; cần BA cung cấp FR đúng. |
| ~~SPEC-CLARIFY-CAUHINH-03~~ | ✅ RESOLVED 2026-05-08 (theo business — KHÔNG có field QH-NT) | Cột QH-NT 200% chỉ ở SCR #10 (UI), không ở FR-VIII-10 Inputs (business). Theo business → cột không có. | srs-fr-10:1641 ✗ vs 457-466 ✓ | TC-CH-SLA-006 convert thành verify cột KHÔNG có. UI render cột → BUG. |
| SPEC-CLARIFY-CAUHINH-04 | ⏳ pending BA | Filter "Phạm vi" cho CB_NV_TW (đã có quyền toàn quốc) ý nghĩa gì? Cả 2 source đều có filter, chỉ semantic chưa rõ. | srs-fr-10:1661 | Test pattern TW dùng filter narrow. |
| ~~SPEC-CLARIFY-CAUHINH-05~~ | ✅ RESOLVED 2026-05-08 (theo business — BR-DATA-06 default 10K) | Business default BR-DATA-06 = 10K rows → áp dụng cho Import ngày lễ. | srs-fr-10:1410 + srs-v3.1.md:5331 | TC-CH-NL-023 test 10K boundary VALID. TC-CH-NL-025 mới: over-10K reject/truncate. |
| SPEC-CLARIFY-CAUHINH-06 | ⏳ pending BA | Calendar view "tùy chọn" — optional cho dev (impl/skip Phase 1) hay cho user (xem được/không)? | srs-fr-10:1417 | TC-CH-NL-030 P2 — defer. |
| SPEC-CLARIFY-CAUHINH-07 | ⏳ pending BA | Race condition save SLA + create HS cùng giây — spec silent. | srs-fr-10:492-493 | Test thực tế Phase B. |
| SPEC-CLARIFY-CAUHINH-08 | ⏳ pending BA | Tab 4 spec field thiếu — gap doc, business chưa cung cấp đủ. | srs-fr-10:1671-1676 | TC happy path basic — defer detailed validation. |
| ~~SPEC-CLARIFY-CAUHINH-09~~ | ✅ RESOLVED 2026-05-08 (BA chốt) | **HOI_DAP SLA = 5 ngày.** FR-VIII-10 seed line 515 đúng. BR-CALC-03 line 5362 viết 15/30 ngày (NĐ55/2019 Đ.8 K.1) là **sai** → cần update SRS, KHÔNG ảnh hưởng test. | srs-fr-10:515 ✓ vs srs-v3.1.md:5362 ✗ | TC-CH-SLA-002 restored: HOI_DAP row test thoi_han=5 ngày như spec FR-VIII-10. |
| ~~SPEC-CLARIFY-CAUHINH-10~~ | ✅ RESOLVED 2026-05-08 (BA chốt — file `phan-hoi-ba-review-srs-fr-02-hoi-dap.md` mục 3) | **BN có thấy mẫu TW.** Permission matrix §3.4.2 MPH_READ đúng. FR-II-NEW-02 Postcondition line 955 viết "BN không thấy TW" là **sai** → cần update SRS, KHÔNG ảnh hưởng test. | srs-v3.1.md:1358 ✓ vs srs-fr-02:955 ✗ | TC-CH-MPH-011 + 069 confirmed: BN thấy mẫu TW + BN own; pattern tương đương DP. |

**Tổng:** **5 SPEC-CLARIFY ✅ RESOLVED** (3 theo business spec rule + 2 BA chốt 2026-05-08), 5 ⏳ pending BA (CAUHINH-02/04/06/07/08 — gap doc / ambiguity).

---

## 6. Liên kết

- SRS Tab 1: `input/srs-v3/srs-fr-10-quan-tri-v3.1.md` lines 440-516 (FR-VIII-10) + 1631-1646 (SCR Tab 1)
- SRS Tab 3: `input/srs-v3/srs-fr-02-hoi-dap-v3.1.md` lines 891-967 (FR-II-NEW-02) + srs-fr-10:1655-1668 (SCR Tab 3)
- SRS Tab 4: `input/srs-v3/srs-fr-10-quan-tri-v3.1.md` lines 1669-1676 (SCR Tab 4 only)
- SRS Ngày lễ: `input/srs-v3/srs-fr-10-quan-tri-v3.1.md` lines 1376-1434
- BR §B.1-B.5: `input/srs-v3/srs-v3.1.md`
- Permission MAU_PHAN_HOI action-level: `srs-v3.1.md §3.4.2`
- Sibling pattern: `output/test-cases/QTHT/Nhat-ky-he-thong/` (W1.1 done 2026-05-08)
- Plan: `Ver3.1/tasks/detailed-tc/plan.md` §3.1 Phase A workflow
