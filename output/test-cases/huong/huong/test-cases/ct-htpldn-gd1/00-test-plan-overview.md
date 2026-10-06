# Kế Hoạch Kiểm Thử — CT HTPLDN Giai đoạn 1 (FR-15, SCR-XI-01)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-06
> **Nguồn dữ liệu**: SRS v3.5 ([srs-fr-15-ct-htpldn-v3.1.md](../../../input/srs-v3/srs-fr-15-ct-htpldn-v3.1.md), kèm [srs-v3.md](../../../input/srs-v3/srs-v3.md) Phụ lục B/C)
> **SRS Reference**: Nhóm XI — UC160..UC165, SCR-XI-01 (Danh sách + Tab Thông tin + Tab Đợt BC)
>
> **Scope GĐ1:** Lifecycle Chương trình HTPLDN (SM-KH-CTHTPL, 8 trạng thái) + CRUD đợt báo cáo (TAO_DOT) — **không** bao gồm Lập BC / Phê duyệt BC / Gửi TW / Tổng hợp (chuyển sang GĐ2 W5.1).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử (GĐ1)

- 6 FR (UC160–UC165) trên 1 màn hình tổng hợp SCR-XI-01.
- Entity chính: `CHUONG_TRINH_HTPL` (owned), `DOT_BAO_CAO` (owned, CRUD lifecycle TAO_DOT)
- State Machine bao quát: **SM-KH-CTHTPL** (8 states: DU_THAO → CHO_PHE_DUYET → DA_DUYET → DA_CONG_BO → DANG_THUC_HIEN → TAM_DUNG → HOAN_THANH / HUY)
- Đặc thù:
  - 7 hành động lifecycle CT (Trình PD, Phê duyệt, Công bố, Kích hoạt, Tạm dừng, Tiếp tục, Hoàn thành, Hủy, Rút trình)
  - Phê duyệt cùng cấp (BR-AUTH-05)
  - Công bố qua API trực tiếp Cổng PLQG (BR-FLOW-05) — fail rollback DA_DUYET
  - CRUD đợt BC chỉ khi CT ở DANG_THUC_HIEN/HOAN_THANH (FR-XI-05a)

### 1.2 Danh sách FR / UC GĐ1

| # | Mã FR | UC | Tên chức năng | Entity | File Test Case |
|---|-------|----|--------------|--------|----------------|
| 1 | FR-XI-01 | UC160 | Quản lý CT HTPL — CRUD core (tạo/sửa/xóa/xem) | CHUONG_TRINH_HTPL | `01-TC-quan-ly-ct-CRUD.md` |
| 2 | FR-XI-02 | UC161 | Tìm kiếm CT HTPL + Xuất Excel | CHUONG_TRINH_HTPL | `02-TC-tim-kiem-ct.md` |
| 3 | FR-XI-01 sub | UC160 | Lifecycle actions CT (Kích hoạt/Tạm dừng/Tiếp tục/Hoàn thành/Hủy/Rút trình) | CHUONG_TRINH_HTPL | `03-TC-lifecycle-ct.md` |
| 4 | FR-XI-03 | UC162 | Trình phê duyệt CT | CHUONG_TRINH_HTPL | `04-TC-trinh-phe-duyet-ct.md` |
| 5 | FR-XI-04 | UC163 | Phê duyệt / Từ chối CT | CHUONG_TRINH_HTPL | `05-TC-phe-duyet-ct.md` |
| 6 | FR-XI-05 | UC164 | Công bố / Hủy công bố CT lên Cổng PLQG | CHUONG_TRINH_HTPL | `06-TC-cong-bo-ct.md` |
| 7 | FR-XI-05a | UC165 | Quản lý đợt báo cáo (CRUD pure, trạng thái TAO_DOT) | DOT_BAO_CAO | `07-TC-quan-ly-dot-bc.md` |
| 8 | — | — | Permission matrix cross-FR-XI GĐ1 | All | `08-TC-permission-matrix.md` |

> **Defer GĐ2 (W5.1):** FR-XI-06 (Lập BC), FR-XI-07 (Trình duyệt BC), FR-XI-07a (Phê duyệt BC), FR-XI-08 (Gửi TW), FR-XI-09 (TW tổng hợp). Lý do: SM-DOT-BC từ DANG_LAP_BC thuộc lifecycle BC, ràng buộc cascade với W3.2 (Vụ việc) + W4.2 (Chi trả) + W4.4 (Đánh giá) cho gợi ý số liệu.

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|----------------------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (toàn HT). `_02` fallback |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD CT TW (toàn quốc). `_02` fallback, `_03` permission test |
| CB_NV_BN | BN | cb_nv_bn_01 (Bộ KH&ĐT) | CRUD CT scoped BN |
| CB_NV_DP | DP | cb_nv_dp_01 (Sở TP AG) | CRUD CT scoped ĐP. `_02` Sở TP BG (cùng cấp khác đơn vị) |
| CB_PD_TW | TW | cb_pd_tw_01 | Phê duyệt CT cùng cấp (TW). KHÔNG CRUD CT |
| CB_PD_BN | BN | cb_pd_bn_01 | Phê duyệt CT scoped BN |
| CB_PD_DP | DP | cb_pd_dp_01 | Phê duyệt CT scoped ĐP. `_02` cùng cấp khác đơn vị (test BR-AUTH-05) |
| NHT/TVV/CG/DN/GV | — | nht_01, tvv_01, cg_01, dn_01 | Negative — verify 403 chặn module |

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng GĐ1? | TC áp dụng |
|----|---------|-----------|--------------|------------|
| BR-AUTH-01 | Xác thực 2-tier (TOTP/SSO) | srs-fr-15:1419 | ✅ | Precondition mọi TC + TC-PERM-006 |
| BR-AUTH-05 | Phê duyệt cùng cấp | srs-fr-15:1428 | ✅ (core) | TC-PD-CT-005, TC-PERM-002 |
| BR-AUTH-08 | Phân quyền theo `don_vi_id` | srs-v3 Phụ lục B | ✅ | TC-CT-CRUD-006, TC-PERM-001/003 |
| BR-DATA-01 | Soft delete (is_deleted=1) | srs-fr-15:1437 | ✅ | TC-CT-CRUD-003, TC-DOT-003 |
| BR-DATA-05 | Audit trail INSERT-only | srs-fr-15:1444 | ✅ | TC-CT-CRUD-001/002/003, TC-LC-001..006, TC-PD-001/004, TC-CB-001/003, TC-DOT-001..003 |
| BR-DATA-06 | Export Excel max 10k rows | srs-v3:3977 | ✅ | TC-CT-TK-006 (boundary), TC-CT-TK-007 (>10k warning) |
| BR-DATA-07 | Pagination 20 default, max 100 | srs-fr-15:1453 | ✅ | TC-CT-CRUD-004, TC-CT-TK-002, TC-DOT-004 |
| BR-FLOW-03 | Không sửa/xóa sau phê duyệt | srs-fr-15:1460 | ✅ (core) | TC-CT-CRUD-011, TC-CT-CRUD-012 |
| BR-FLOW-04 | Từ chối yêu cầu lý do | srs-fr-15:1467-1471 | ✅ (core) | TC-PD-CT-003 (Codex fix 2026-05-09: bỏ TC-LC-008 — BR-FLOW-04 chỉ áp Từ chối, không Tạm dừng. ERR-XI-01-TD-03 là rule riêng FR-XI-01 Tạm dừng line 226) |
| BR-FLOW-05 | Công khai qua API trực tiếp Cổng PLQG | srs-fr-15:1474 | ✅ (core) | TC-CB-001..005 |
| BR-EC-01 | Optimistic Locking | srs-v3:4066 | ✅ | TC-CT-CRUD-013 (concurrent UPDATE) |
| BR-EC-12 | Pagination guard `[1,100]` | srs-v3:4077 | ✅ | TC-CT-TK-009 (param boundary) |
| BR-EC-13 | Search sanitize max 200 ký tự + escape | srs-v3:4078 | ✅ | TC-CT-TK-010, TC-CT-TK-011 (SQL/XSS) |
| BR-EC-19 | Batch ops max 100 records | srs-v3:4084 | (chỉ GĐ2 — TW tổng hợp) | — |
| **SM-KH-CTHTPL** | State machine 8 states + 12 transitions | srs-fr-15:1331-1370 | ✅ (core) | All file 03-06 + lifecycle TC trong 01 |

**Coverage GĐ1:** 14 BR áp dụng (loại BR-EC-19 thuộc GĐ2).

### 2.2 Error Codes / Warnings

**FR-XI-01 (CRUD CT):** ERR-XI-01-01 (thiếu trường), ERR-XI-01-02 (sửa CT ≠ DU_THAO), ERR-XI-01-03 (xóa CT ≠ DU_THAO)
**FR-XI-01 sub-actions:**
- Kích hoạt: ERR-XI-01-KH-01 (không quyền), ERR-XI-01-KH-02 (CT ≠ DA_DUYET/DA_CONG_BO)
- Tạm dừng: ERR-XI-01-TD-01..03, WRN-XI-01-TD-01 (có đợt BC đang lập)
- Tiếp tục: ERR-XI-01-TT-01..02
- Hoàn thành: ERR-XI-01-HT-01..03 (E3 = còn đợt BC chưa hoàn thành)
- Hủy: ERR-XI-01-HC-01..02
- Rút trình: ERR-XI-01-RT-01..02

**FR-XI-02 (Tìm kiếm + Export):** INF-CT-TK-01 (no result), INF-XI-02-XL-01 (DS trống), WRN-XI-02-XL-01 (>10k rows)
**FR-XI-03 (Trình PD):** ERR-XI-03-01 (CT ≠ DU_THAO)
**FR-XI-04 (Phê duyệt):** ERR-XI-04-01 (CT ≠ CHO_PHE_DUYET), ERR-XI-04-02 (TC thiếu lý do), ERR-XI-04-03 (CB PD khác cấp)
**FR-XI-05 (Công bố):** ERR-XI-05-01 (CT ≠ DA_DUYET), ERR-XI-05-02 (API Cổng lỗi)
**FR-XI-05a (CRUD đợt BC):** ERR-XI-05a-01 (CT ≠ DANG_THUC_HIEN/HOAN_THANH), ERR-XI-05a-02 (đợt trùng kỳ), ERR-XI-05a-03 (xóa đợt ≠ TAO_DOT)

### 2.3 Permission Matrix (GĐ1)

| Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV/CG/DN |
|--------|------|------------------|-------------------|---------------|
| CT — CRUD (DU_THAO only) | 👁️ R | ✅ CRUD\* (scope) | 👁️ R\* (xem) | ❌ |
| CT — Trình PD (FR-XI-03) | ❌ | ✅ | ❌ | ❌ |
| CT — Phê duyệt (FR-XI-04) | ❌ | ❌ | ✅ (cùng cấp) | ❌ |
| CT — Công bố / Hủy CB (FR-XI-05) | ❌ | ✅ | ❌ | ❌ |
| CT — Kích hoạt | ❌ | ✅ | ❌ | ❌ |
| CT — Tạm dừng / Tiếp tục (Codex fix 2026-05-09) | ❌ | ✅ | ✅ | ❌ |
| CT — Hoàn thành | ❌ | ❌ | ✅ | ❌ |
| CT — Hủy / Rút trình | ❌ | ✅ (người tạo / người trình) | ❌ | ❌ |
| Đợt BC — CRUD (TAO_DOT only) | 👁️ R | ✅ CRUD\* (scope) | 👁️ R | ❌ |

(\* = bị giới hạn theo `don_vi_id` của user, BR-AUTH-08)

> **Footnote Codex review 2026-05-09 (ROLE-001):** SRS srs-fr-15:213 + 241 nguyên văn `Kiểm tra quyền CB NV/CB PD` cho cả Tạm dừng và Tiếp tục → CẢ HAI role được phép. Matrix v1 trước đây gán chỉ CB_PD là sai, đã sửa. Test bổ sung TC-LC-004b/007b (CB_NV positive) + TC-LC-004c/007c (NHT/TVV/CG negative) trong file 03.

### 2.4 State Machine — SM-KH-CTHTPL

```
[*] → DU_THAO
  DU_THAO ↔ CHO_PHE_DUYET (Trình ↔ Rút trình hoặc PD Từ chối)
  CHO_PHE_DUYET → DA_DUYET (PD duyệt cùng cấp)
  DA_DUYET ↔ DA_CONG_BO (Công bố / Hủy CB qua API Cổng PLQG)
  DA_DUYET / DA_CONG_BO → DANG_THUC_HIEN (Kích hoạt)
  DANG_THUC_HIEN ↔ TAM_DUNG (Tạm dừng có lý do / Tiếp tục)
  DANG_THUC_HIEN → HOAN_THANH (CB PD, guard: tất cả đợt BC đã hoàn thành)
  DU_THAO → HUY
```

### 2.5 SM-DOT-BC (chỉ TAO_DOT trong GĐ1)

```
[*] → TAO_DOT (CRUD pure trong GĐ1)
  TAO_DOT → DANG_LAP_BC  ← (Defer GĐ2: bắt đầu lập BC)
```

GĐ1 **chỉ test** transition `[*] → TAO_DOT` (tạo / sửa / xóa đợt BC khi TAO_DOT). Phần `TAO_DOT → DANG_LAP_BC → ... → DA_TONG_HOP` thuộc GĐ2.

---

## 3. Cấu Trúc File Test Case (dự kiến — sau A4/A6/A7 inline merge)

```
ct-htpldn-gd1/
├── 00-test-plan-overview.md           ← (file này)
├── 01-TC-quan-ly-ct-CRUD.md           ← FR-XI-01 UC160 CRUD core (~11 TC)
├── 02-TC-tim-kiem-ct.md               ← FR-XI-02 UC161 search + export Excel (~11 TC)
├── 03-TC-lifecycle-ct.md              ← FR-XI-01 sub-actions: Kích hoạt/Tạm dừng/Tiếp tục/Hoàn thành/Hủy/Rút trình (~15 TC)
├── 04-TC-trinh-phe-duyet-ct.md        ← FR-XI-03 UC162 (~6 TC)
├── 05-TC-phe-duyet-ct.md              ← FR-XI-04 UC163 (~9 TC)
├── 06-TC-cong-bo-ct.md                ← FR-XI-05 UC164 (~8 TC)
├── 07-TC-quan-ly-dot-bc.md            ← FR-XI-05a UC165 CRUD đợt BC (~8 TC)
├── 08-TC-permission-matrix.md         ← Permission cross-FR-XI GĐ1 (~6 TC)
├── 09-REVIEW-edge-case-hunter.md      ← A4 audit log (đã merge edge case vào 01-08)
├── 10-traceability-matrix.md          ← A5 BR/AC ↔ TC matrix
├── 11-REVIEW-test-quality.md          ← A6 6-axis quality score
└── 12-a7-filter-log.md                ← A7 filter log
```

> **Phase B B-block ref CHỈ 8 file UC (01-08)**, dự kiến ~74 TC sau A3 + thêm sau A4/A6 → 85 TC sau A4/A6 → **100 TC sau Codex review 2026-05-09 (+15 TC)**. File 09-12 là audit log.

### 3.1 File counts breakdown (sau Codex 2026-05-09)

| File | Original | A4/A6 added | Codex added | Final |
|------|---------:|------------:|------------:|------:|
| 01 - CT CRUD | 11 | +4 | 0 | 15 |
| 02 - Tìm kiếm CT | 11 | +1 | 0 | 12 |
| 03 - Lifecycle CT | 15 | +2 | +10 | 27 |
| 04 - Trình PD CT | 6 | 0 | 0 | 6 |
| 05 - Phê duyệt CT | 9 | +1 | 0 | 10 |
| 06 - Công bố CT | 8 | +1 | 0 | 9 |
| 07 - Đợt BC | 8 | +2 | +2 | 12 |
| 08 - Permission | 6 | 0 | +3 | 9 |
| **TỔNG** | **74** | **+11** | **+15** | **100** |

> **Codex 2026-05-09 changelog:**
> - **ERR codes (file 03):** +7 TC fill 7 ERR thiếu (KH-01, TD-01, TD-02, TT-01, HT-02, HC-01, RT-02).
> - **Role correction (file 03):** +2 TC CB_NV Tạm dừng/Tiếp tục (per SRS 213/241 cho phép cả CB_NV); +1 SPEC-CLARIFY-CT-05 Kích hoạt guard.
> - **Đợt BC (file 07):** +2 TC (DOT-011 sửa state guard, DOT-012 thiếu trường bắt buộc).
> - **Permission Matrix (file 08):** +3 TC (PERM-007 CB_PD Read positive, PERM-008 CB_PD negative Hủy/Rút trình/Công bố, PERM-009 QTHT Read-only lifecycle).
> - **Đã sửa:** TC-LC-005 (file 03) — bỏ ref `BR-FLOW-04` không phù hợp. TC-CT-TK-007 (file 02) — đổi `BR-DATA-06` → `BR-DATA-07` per srs-fr-15:395. Matrix §2.3 row Tạm dừng/Tiếp tục — gán cả CB_NV (was CB_PD only).
> - **SPEC-CLARIFY mới:** CT-05 (Kích hoạt guard "kế hoạch chi tiết" UI mapping), CT-06 (ERR code cho sửa đợt sai state).
> - **Coverage sau Codex:** ERR codes 30/30 = 100% (was 23/30 = 77%); Permission Matrix ~30/32 cells (was 24/32 = 75%); SM/AC/BR đã 100%.

---

## 4. Strategy đặc thù module

- **Sub-action density (file 03):** FR-XI-01 chứa 7 sub-process (CRUD + Kích hoạt + Tạm dừng + Tiếp tục + Hoàn thành + Hủy + Rút trình). Tách CRUD core (file 01) khỏi lifecycle actions (file 03) để Phase B B-block dễ chạy + dễ trace bug per transition.
- **Approval cross-cấp (BR-AUTH-05):** Cần TK fallback `cb_pd_dp_02` (Sở TP BG) để test "CB PD ĐP duyệt CT của ĐP khác đơn vị" → expected ERR-XI-04-03.
- **API Cổng PLQG (BR-FLOW-05):** TC TC-CB-002 verify rollback khi API external fail. Test qua MCP `list_network_requests` — quan sát response code (5xx/timeout) + UI rollback DA_DUYET.
- **Hoàn thành CT guard:** TC TC-LC-005 require pre-seed 1 đợt BC ở DA_TONG_HOP (cuối lifecycle GĐ2). Trong GĐ1 chỉ verify error case "còn đợt BC chưa hoàn thành" (ERR-XI-01-HT-03), happy path defer GĐ2 hoặc seed cross-phase.
- **Đợt BC trùng kỳ (FR-XI-05a):** TC TC-DOT-004 test combination key `(chuong_trinh_id, ky_bao_cao, tu_ngay-den_ngay)` unique → ERR-XI-05a-02.
- **Filter A7 dự kiến:** Toàn bộ TC chạy qua UI SCR-XI-01 + verify network qua MCP → 0 TC chỉ-DB/API thuần. AC liên quan API outbound (TC TC-CB-001 push Cổng) verify gián tiếp qua `list_network_requests` xem URL/payload outbound — vẫn UI-driven.

---

## 5. Acceptance Phase A

- ✅ 7 bước A1-A7 done
- ✅ Traceability ≥95% BR (loại BR-EC-19 thuộc GĐ2) + 100% AC
- ✅ 0 TC chỉ-DB/API thuần (A7 verified)
- ✅ 0 TC sống ở file phụ 08-11 (mọi TC inline trong file UC 01-07)
- ✅ SPEC-CLARIFY listed (gửi BA Phase B)
- ✅ Codex review 2026-05-09 GATE FAIL → patched (3 P0 + 4 P1 + 3 P2 đã fix; 100% ERR codes; ~94% Permission Matrix cells)

## 6. SPEC-CLARIFY pending BA sign-off

| # | ID | Mô tả | TC liên quan | Nguồn |
|---|----|-------|--------------|-------|
| 1 | SPEC-CLARIFY-CT-01 | BR-AUTH-05 cùng cấp ĐP cross-đơn vị (Sở TP AG vs Sở TP BG) | TC-PD-CT-005 | srs-fr-15:1428-1435 |
| 2 | SPEC-CLARIFY-CT-02 | han_nop strict deadline TT17 vs info-only | TC-DOT-BC-008 | srs-fr-15:88-94 |
| 3 | SPEC-CLARIFY-CT-04 | Công bố CT đã hết hạn — PASS / WARN / REJECT | TC-CB-CT-009 | srs-fr-15:548-608 |
| 4 | SPEC-CLARIFY-CT-05 (Codex 2026-05-09) | Kích hoạt CT guard "kế hoạch chi tiết, đơn vị thực hiện" — field UI mapping | TC-LC-003c | srs-fr-15:191 |
| 5 | SPEC-CLARIFY-CT-06 (Codex 2026-05-09) | ERR code cho "sửa đợt BC sai state" — reuse ERR-XI-05a-03 hay tạo mới | TC-DOT-BC-011 | srs-fr-15:656 |

---

*Generated 2026-05-06 — Phase A step A2 (bmad-testarch-test-design) · Updated 2026-05-09 sau Codex review (+15 TC, 5 SPEC-CLARIFY).*
