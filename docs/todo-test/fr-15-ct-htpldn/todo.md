# TODO — FR-15 — CT HTPLDN GĐ1+GĐ2

> **Module:** FR-15 — Quản lý kế hoạch thực hiện CT HTPLDN (đổi tên A-ITEM-13 v3.5)
> **Phân nhóm v3.5:** **B — DELTA+IMPACT** (8 thay đổi cherry-pick từ v4 áp v3.5, ref CHANGELOG line 2508-2640)
> **Test plan:** [`test-plan.md`](test-plan.md) v1.1 (Revised 2026-05-12 12:35:00)
> **SRS:** `input/srs-v3/srs-fr-15-ct-htpldn.md` + `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` line 2508-2640
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream
> **Ngày tạo:** 2026-05-12 12:40:00

---

## Tổng hợp

| Nhóm | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| GĐ1 KH năm — CRUD + 3 core field | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| GĐ1 KH năm — Lifecycle KH duyệt + 6 actions | 4 | 4 | 0 | 0 | 0 | 0 | 0 |
| GĐ2 DOT_BAO_CAO CRUD + datepicker | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| GĐ2 — Lifecycle Đợt BC (BC KQ + Gửi TW + Tổng hợp) | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| 5 audit fields verify DOT_BAO_CAO | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| Cross-cutting CR-01 verify (FR-15 GIỮ `la_cong_bo`) | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| Permission cross-cấp + DN/NHT negative | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| **Tổng** | **15** | **15** | **0** | **0** | **0** | **0** | **0** |

---

## Tasks

### Nhóm 1 — GĐ1 KH năm: CRUD + 3 trường core bắt buộc [GAP-XI-03]

- 🟢 **T-FR15-001** UC160 — CRUD KH HTPLDN scope DU_THAO (test-case `01-TC-crud-ct.md` happy + edit/delete BR-FLOW-03)
  - **Cần có sẵn:** [need: DM CHUONG_TRINH_HT ≥3 variants TW/BN/ĐP (✗ chờ T-FR10-XXX seed DM); ≥5 DN HOAT_DONG (✗ chờ T-FR07-XXX); CB NV TW/BN/ĐP _01/_02 active]
  - **Kết quả:** chưa run.
  - **Output:** `output/qa-reports/round{N}/functional/ct-htpldn/functional-test-report-fr15-001.md`

- 🟢 **T-FR15-002** UC160 — Negative `muc_tieu`/`doi_tuong`/`thoi_gian_bat_dau` BẮT BUỘC [GAP-XI-03] + ERR-XI-01-01
  - **Cần có sẵn:** [need: CB NV TW/BN/ĐP _01 login; DM CT seed ≥1 (✗ chờ T-FR10-XXX)]
  - **Kết quả:** chưa run.
  - **Output:** trace ref CHANGELOG Thay đổi 6 (`[GAP-XI-03]`) — POST CT thiếu 1 trong 3 trường → reject + ERR-XI-01-01

### Nhóm 2 — GĐ1 KH năm: Lifecycle KH duyệt + 6 actions [GAP-XI-01]

- 🟢 **T-FR15-003** UC161 — Tìm kiếm + Xuất Excel `[GAP-XI-04]` (5 step + boundary 10K + danh sách rỗng)
  - **Cần có sẵn:** [need: ≥20 CT HTPLDN trong DB cover cấp TW/BN/ĐP (✗ chờ T-FR15-001 seed); CB NV TW _01]
  - **Kết quả:** chưa run.

- 🟢 **T-FR15-004** UC162 + UC163 — Trình duyệt + Duyệt/Từ chối KH (BR-AUTH-05 cùng cấp)
  - **Cần có sẵn:** [need: ≥3 CT DU_THAO mỗi cấp (TW/BN/ĐP) (✗ chờ T-FR15-001); CB PD TW/BN/ĐP _01 + cross-unit _02 (cb_pd_bn_02 BTC + cb_pd_dp_02 BG)]
  - **Kết quả:** chưa run.

- 🟢 **T-FR15-005** 🆕 v3.5 — Lifecycle actions 6 hành động `[GAP-XI-01]` (test-case `12-TC-lifecycle-actions.md`): Kích hoạt / Tạm dừng / Tiếp tục / Hủy / **Rút trình → DU_THAO** (KHÔNG → HUY)
  - **Cần có sẵn:** [need: ≥1 CT mỗi state DA_DUYET / DA_CONG_BO / DANG_THUC_HIEN / TAM_DUNG / CHO_PHE_DUYET (✗ chờ T-FR15-004 advance state); CB NV tạo CT ban đầu (verify "CB NV tạo ban đầu" guard rút trình)]
  - **Kết quả:** chưa run.
  - **Output:** ref CHANGELOG Thay đổi 4 Phần 3 — `CHO_PHE_DUYET → DU_THAO` (form giữ nội dung)

- 🟢 **T-FR15-006** 🆕 v3.5 — **Hoàn thành KH = CB PD** (KHÔNG CB NV) + guard "Tất cả đợt BC đã hoàn thành" `[GAP-XI-01]`
  - **Cần có sẵn:** [need: ≥1 CT state DANG_THUC_HIEN có ≥1 Đợt BC TAO_DOT (test guard fail) + ≥1 CT có all Đợt BC DA_TONG_HOP (test happy); CB NV _01 (test negative actor) + CB PD _01 cùng cấp (test happy)]
  - **Kết quả:** chưa run.
  - **Output:** ref CHANGELOG Thay đổi 4 Phần 2 — login CB NV ấn Hoàn thành → "Chỉ CB PD mới được hoàn thành chương trình"; login CB PD + còn TAO_DOT → block; CB PD + all DA_TONG_HOP → PASS HOAN_THANH

### Nhóm 3 — GĐ2 DOT_BAO_CAO: CRUD + datepicker DATE-ONLY [SRS-FIX]

- 🟢 **T-FR15-007** UC165 — CRUD Đợt BC + BR-XI-DOT-DUP + state guard CT (BR-XI-CT-STATE-DOT)
  - **Cần có sẵn:** [need: ≥3 CT state DANG_THUC_HIEN (✗ chờ T-FR15-005 advance); ≥1 CT DU_THAO (test guard fail ERR-XI-05a-01); CB NV TW/BN/ĐP _01]
  - **Kết quả:** chưa run.

- 🟢 **T-FR15-008** 🆕 v3.5 — Modal tạo Đợt BC: datepicker DATE-ONLY cho `han_nop` / `tu_ngay` / `den_ngay` `[SRS-FIX]` + dropdown kỳ BC 3 giá trị TT17 `[GAP-XI-02]`
  - **Cần có sẵn:** [need: ≥1 CT DANG_THUC_HIEN (✗ chờ T-FR15-005); CB NV TW _01]
  - **Kết quả:** chưa run.
  - **Output:** verify UI KHÔNG render ô giờ-phút trên picker; POST `ky_bao_cao=THANG` → reject 400; chỉ accept `SO_BO_6_THANG/SO_BO_NAM/TRON_NAM`

### Nhóm 4 — GĐ2 Lifecycle Đợt BC (BC KQ + Gửi TW + Tổng hợp)

- 🟢 **T-FR15-009** UC166 + UC167 + UC168 — Lập BC 21a/21b + trình duyệt + CB PD duyệt KQ (BR-AUTH-05 BC)
  - **Cần có sẵn:** [need: ≥3 Đợt BC DANG_LAP_BC mỗi cấp (✗ chờ T-FR15-008); CB NV + CB PD TW/BN/ĐP _01 same cấp; số liệu cross-module VV/Chi trả/Đào tạo trong kỳ (✗ chờ T-FR05/06/03)]
  - **Kết quả:** chưa run.

- 🟢 **T-FR15-010** UC169 — BN/ĐP gửi TW + ERR-XI-08-02 (TW ấn Gửi TW → reject)
  - **Cần có sẵn:** [need: ≥1 Đợt BC DA_DUYET_KQ mỗi cấp BN + ĐP (✗ chờ T-FR15-009); CB NV BN _01 + CB NV ĐP _01 + CB NV TW _01 (test negative)]
  - **Kết quả:** chưa run.

- 🟢 **T-FR15-011** UC170 — TW tổng hợp BC toàn quốc + xuất Excel/Word TT17 + ERR-XI-09-01 + ERR-XI-09-02
  - **Cần có sẵn:** [need: ≥2 Đợt BC DA_GUI_TW từ BN/ĐP (✗ chờ T-FR15-010); CB NV TW _01 (happy + tổng hợp 0 BC test ERR-XI-09-01); CB NV BN _01 (test ERR-XI-09-02)]
  - **Kết quả:** chưa run.

### Nhóm 5 — 5 audit fields verify [SRS-FIX]

- 🟢 **T-FR15-012** 🆕 v3.5 — Verify 5 audit fields DOT_BAO_CAO (`created_at` / `updated_at` / `created_by` / `updated_by` / `is_deleted`) ghi đúng người + thời điểm
  - **Cần có sẵn:** [need: ≥1 Đợt BC vừa create + ≥1 Đợt BC vừa update bởi user khác (✗ chờ T-FR15-007); CB NV _01 + _02 same cấp để verify `updated_by` đổi sau khi user _02 sửa]
  - **Kết quả:** chưa run.
  - **Output:** test-case `13-TC-dot-bc-audit-fields.md` — GET `/dot-bao-cao/{id}` verify 5 fields render đúng; DELETE → `is_deleted=1` (soft); response 3 trường ngày là string `YYYY-MM-DD` (KHÔNG có suffix `T00:00:00`)

### Nhóm 6 — Cross-cutting CR-01 verify (FR-15 GIỮ `la_cong_bo`)

- 🟢 **T-FR15-013** Verify FR-15 GIỮ `la_cong_bo` v3 (CR-01 KHÔNG áp module này — CHANGELOG line 2508-2640 không list rename)
  - **Cần có sẵn:** [need: ≥1 CT DA_CONG_BO (✗ chờ T-FR15-005); CB NV TW _01]
  - **Kết quả:** chưa run.
  - **Output:** GET `/chuong-trinh-htpl/{id}` response phải có field `la_cong_bo: boolean` + `ngay_cong_bo: datetime`. **KHÔNG log bug nếu thiếu field `cong_khai`/`nguoi_cong_khai`** — verdict v3.5 verified.

### Nhóm 7 — Permission cross-cấp + DN/NHT negative

- 🟢 **T-FR15-014** Permission negative cross-cấp BR-AUTH-05 — CB PD khác cấp duyệt CT/BC → ERR-XI-04-03 / ERR-XI-07a-03
  - **Cần có sẵn:** [need: ≥1 CT CHO_PHE_DUYET cấp BN + ≥1 BC CHO_DUYET_KQ cấp ĐP (✗ chờ T-FR15-004 + T-FR15-009); CB PD TW _01 (test cross-cấp); CB PD BN _02 BTC + CB PD ĐP _02 BG (test cross-unit cùng cấp)]
  - **Kết quả:** chưa run.

- 🟢 **T-FR15-015** Permission negative DN + NHT/CG/TVV → KHÔNG được CRUD/duyệt KH HTPLDN + Breadcrumb verify A-ITEM-13
  - **Cần có sẵn:** [need: ≥1 CT DA_CONG_BO (test public view DN có thấy không); DN test account `9999999990` + NHT `nht_01` + CG `cg_01` + TVV `tvv_01`]
  - **Kết quả:** chưa run.
  - **Output:** verify sidebar role DN/NHT/CG/TVV KHÔNG render menu "Quản lý kế hoạch thực hiện CT HTPLDN"; navigate direct URL → 403; verify Breadcrumb text v3.5 (A-ITEM-13)

---

## Cross-module dependencies (state-explicit)

| Entity cần | State target | Module owner | Task downstream FR-15 cần state này |
|---|---|---|---|
| `DM CHUONG_TRINH_HT` | ≥3 records, active | FR-10 Quản trị (T-FR10-XXX) | T-FR15-001, T-FR15-002 |
| `DOANH_NGHIEP` | ≥5 records, `HOAT_DONG` | FR-07 DN (T-FR07-XXX) | T-FR15-001 |
| Tài khoản CB NV TW/BN/ĐP `_01/_02` | active, role chuẩn | FR-10 Quản trị / FR-08 Phân quyền | Tất cả task |
| Tài khoản CB PD TW/BN/ĐP `_01/_02` (BTC + BG cho cross-unit) | active, role chuẩn | FR-10 / FR-08 | T-FR15-004, T-FR15-006, T-FR15-009, T-FR15-014 |
| Số liệu VV / Chi trả `DA_THANH_TOAN` / Đào tạo `HOAN_THANH` trong kỳ | đủ data cross-module | FR-05 / FR-06 / FR-03 | T-FR15-009 (Lập BC) |
| `DM LINH_VUC_HTPL`, `DM TINH_TRANG_KH` | ≥3 active | FR-10 | T-FR15-001 |

---

## Note

- **Note 2026-05-12 12:40:00 — Phân nhóm B+ scope:** Test plan đã re-classify nhóm C → B sau review. 15 task này bao phủ 8 thay đổi v3.5 (A-ITEM-13 module rename + B2d UC re-numbering + A-ITEM-09 audit/date + 5 B1 lifecycle/Excel/core field/enum/DON_VI). Khi execute round QA cụ thể, ưu tiên T-FR15-005 + T-FR15-006 + T-FR15-008 + T-FR15-012 (cluster v3.5 mới).
- **Reference round trước:** Tasks R7.6.4, R7.6.5, R7.7.15, R7.7.15.b, R7.E2 đã PASS happy path v3 ở `tasks/todo-ct-htpldn.md`. Bộ T-FR15-XXX này là **delta verification cho v3.5** — không re-run toàn bộ happy path đã PASS.
- **Cấm:**
  - Mark task "Sai spec" / "BLOCK chờ BA" cho field `la_cong_bo` — verdict v3.5 đã chốt FR-15 GIỮ.
  - Test datepicker `han_nop` với input chuỗi datetime — kiểm tra reject 400.
  - Hoàn thành CT bằng CB NV — phải dùng CB PD.

---

*TODO generated 2026-05-12 12:40:00 — module FR-15 nhóm B v3.5, 15 task cover 8 thay đổi cherry-pick CHANGELOG line 2508-2640. Cross-module dep state-explicit theo [feedback_dependency_chain_state_explicit].*
