# TODO — FR-08 — Theo dõi Đánh giá HQ HTPL (rename v3.5)

> Module letter: L (M12). SRS: `input/srs-update-2026-5-5/srs-fr-08-danh-gia.md` (FR-VI-01..10, SCR-VI-01).
> Test plan: [`test-plan.md`](test-plan.md) v1.1 (Revised 2026-05-12 13:30:00) — 50 TC × 13 file.
> SM 8 state canonical v3.5: `LAP_KE_HOACH → PHAN_CONG → CHO_DUYET_PC → THUC_HIEN → BAO_CAO → CHO_PHE_DUYET → HOAN_THANH` + `HUY` terminal.
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream
>
> **Cross-module dep gates (state-explicit per CLAUDE.md state marker workflow):**
> - `[need: ≥3 VV HOAN_THANH (✗ chờ T-FR05-XXX seed VV `HOAN_THANH` ≥3 record per cấp scope `don_vi_id`)]`
> - `[need: ≥1 set DM TIEU_CHI_DG_HQ (✗ chờ T-FR10-XXX seed DM nhóm TIEU_CHI_DG_HQ ≥4 tiêu chí với trọng số cover 100%)]`
> - `[need: ≥2 DON_VI cùng cấp + ≥1 DON_VI cấp dưới (✗ chờ T-FR09-XXX seed BTP-TW + STP-AG + STP-BG để test FR-VI-10 cross-unit)]`
> - `[need: ≥6 TAI_KHOAN role CB_NV + CB_PD theo 3 cấp TW/BN/ĐP (✗ chờ T-FR12-XXX seed account 3 cấp)]`

---

## Tasks

- 🟢 **T-FR08-001** Seed `KE_HOACH_DANH_GIA` entry `LAP_KE_HOACH` ≥3 variant
  - **Mô tả:** Tạo KH ĐG mới ≥3 variant qua UI FR-VI-01 — cover 2 tần suất (SO_BO_6_THANG/TRON_NAM) × 2 đối tượng (VU_VIEC/DAO_TAO) × 2 vai trò cơ quan (don_vi_id ≠ co_quan_duoc_danh_gia_id) + file_dinh_kem ≥1 file/variant. Auto-gen mã `DG-{YYYYMMDD}-{SEQ}` (BR-DATA-04).
  - **Acceptance:** 3 KH state `LAP_KE_HOACH` + verify `co_quan_duoc_danh_gia_id` NOT NULL (Required=Y line 1017) + mã đúng format + 7 common field đủ (BR-DATA-03).
  - **Cần có sẵn:** `[need: ≥2 DON_VI cùng cấp + ≥1 DON_VI cấp dưới (✗ chờ T-FR09-XXX)]`, `[need: ≥3 TAI_KHOAN CB_NV (✗ chờ T-FR12-XXX)]`
  - **Spec:** FR-VI-01 line 1006-1018, BR-DATA-04 line 1209-1213

- 🟢 **T-FR08-002** Seed `TIEU_CHI_DANH_GIA` Σ trọng số = 100% per KH
  - **Mô tả:** Trên Tab 1 mỗi KH seeded T-FR08-001, thêm ≥4 tiêu chí từ DM `TIEU_CHI_DG_HQ` sao cho Σ trọng số = 100% (vd 30/30/20/20). Verify label tổng trọng số 🟢 + KHÔNG có alert WRN-TC-01.
  - **Acceptance:** Mỗi KH có ≥4 row `TIEU_CHI_DANH_GIA` + Σ = 100.00% (tolerance ±0.01% BR-CALC-04).
  - **Cần có sẵn:** `[need: T-FR08-001 (✓ 3 KH state LAP_KE_HOACH)]`, `[need: ≥1 set DM TIEU_CHI_DG_HQ (✗ chờ T-FR10-XXX)]`
  - **Spec:** FR-VI-02, BR-CALC-04 line 1221-1225

- 🟢 **T-FR08-003** Workflow advance state — `LAP_KE_HOACH → PHAN_CONG → CHO_DUYET_PC`
  - **Mô tả:** UI walk: phân công ≥1 TRUONG_NHOM + ≥1 DANH_GIA_VIEN (FR-VI-03) → trình duyệt PC. Verify TB gửi CB PD cùng cấp (BR-NOTIF-01 mở rộng v3.5).
  - **Acceptance:** ≥2 KH state `CHO_DUYET_PC` + verify `PHAN_CONG_DANH_GIA` record (hoặc sub-table per SPEC-CLARIFY-FR08-08) + AUDIT_LOG INSERT.
  - **Cần có sẵn:** `[need: T-FR08-002 (✓ 2 KH có tiêu chí 100%)]`, `[need: ≥2 CB_PD cùng cấp (✗ chờ T-FR12-XXX)]`
  - **Spec:** FR-VI-03, FR-VI-04, BR-NOTIF-01 line 1239-1243

- 🟢 **T-FR08-004** Workflow advance state — `CHO_DUYET_PC → THUC_HIEN` (CB PD duyệt)
  - **Mô tả:** CB PD cùng cấp đăng nhập, duyệt PC qua Tab 2 action [Phê duyệt PC]. Verify TB gửi CB NV creator. Test BR-AUTH-05 cùng cấp + reject xuyên cấp (TC-DG-14).
  - **Acceptance:** ≥2 KH state `THUC_HIEN` + KH BN không bị CB PD TW duyệt được (403).
  - **Cần có sẵn:** `[need: T-FR08-003 (✓ 2 KH CHO_DUYET_PC)]`
  - **Spec:** FR-VI-04, BR-AUTH-05 line 1197-1201

- 🟢 **T-FR08-005** Seed VV `HOAN_THANH` ∪ `DA_DANH_GIA` cho FR-VI-05 (cross-module)
  - **Mô tả:** Walk workflow FR-05 tạo VV state `HOAN_THANH` ≥3 record + advance ≥1 sang `DA_DANH_GIA` qua KH khác để test multi-select + cảnh báo. `ngay_hoan_thanh ∈ [tu_ngay, den_ngay]` của KH FR-08. Filter scope `don_vi_id` user.
  - **Acceptance:** ≥3 VV `HOAN_THANH` + ≥1 VV `DA_DANH_GIA` (verify SRS:858 "Hoàn thành hoặc Đã đánh giá"). Dropdown FR-VI-05 hiện đủ.
  - **Cần có sẵn:** `[need: ≥3 VV HOAN_THANH (✗ chờ T-FR05-XXX seed VV HOAN_THANH ≥3 record per scope)]`
  - **Spec:** BR-VI-08-03 line 858, system-overview line 603/834

- 🟢 **T-FR08-006** Chọn VV + Chấm điểm TT17 → `BAO_CAO`
  - **Mô tả:** Tab 3 multi-select VV `HOAN_THANH` ∪ `DA_DANH_GIA` + chấm điểm inline tất cả tiêu chí (0-`diem_toi_da`). Verify auto-calc `điểm tổng = Σ(diem_i × trong_so_i / 100)` + xếp loại 4 mức (≥90/≥70/≥50/<50). Sau chấm hết → click [Hoàn tất chấm điểm] → `BAO_CAO`.
  - **Acceptance:** ≥1 KH state `BAO_CAO` + ≥3 record `KET_QUA_DANH_GIA` per KH + boundary calc đúng (TC-DG-21a/21b).
  - **Cần có sẵn:** `[need: T-FR08-004 (✓ 1 KH THUC_HIEN)]`, `[need: T-FR08-005 (✓ ≥3 VV HOAN_THANH scope khớp)]`
  - **Spec:** FR-VI-05/06, BR-CALC-04, BR-VI-08-04 line 860

- 🟢 **T-FR08-007** Lập BC + Trình duyệt BC → `CHO_PHE_DUYET`
  - **Mô tả:** Tab 4 verify KPI cards (tổng VV / điểm TB / SLA) + Radar/Bar chart + nhận xét chung. Click [Trình duyệt BC] → state `CHO_PHE_DUYET` + TB CB PD (BR-NOTIF-01).
  - **Acceptance:** ≥1 KH state `CHO_PHE_DUYET` + `BAO_CAO_DANH_GIA` record tạo với `mau_bao_cao ∈ {MAU_21A, MAU_21B}` (line 1058).
  - **Cần có sẵn:** `[need: T-FR08-006 (✓ 1 KH BAO_CAO)]`
  - **Spec:** FR-VI-07/08

- 🟢 **T-FR08-008** Phê duyệt BC → `HOAN_THANH` + xuất XLSX/DOCX TT17
  - **Mô tả:** CB PD cùng cấp click [Phê duyệt BC] → `HOAN_THANH`. Xuất XLSX (Mẫu 21a TT17) + DOCX (Mẫu 21b) — verify nội dung cell A1/heading match template TT17/2025.
  - **Acceptance:** ≥1 KH state `HOAN_THANH` + file XLSX/DOCX download được + nội dung khớp mẫu (TC-DG-23a).
  - **Cần có sẵn:** `[need: T-FR08-007 (✓ 1 KH CHO_PHE_DUYET)]`
  - **Spec:** FR-VI-09, BR-DATA-06

- 🟢 **T-FR08-009** FR-VI-10 — Read-only cross-unit (CB NV `co_quan_duoc_danh_gia_id`)
  - **Mô tả:** Đăng nhập CB NV của cơ quan được ĐG (vd `cb_nv_dp_01` AG khi KH `co_quan_duoc_danh_gia_id=STP-AG`). Verify SCR-VI-01 truy cập được Tab Báo cáo read-only khi KH `HOAN_THANH`. Test matrix 4 pair: TW×ĐP, BN×BN, BN×ĐP, ĐP×ĐP (TC-DG-26/29/29a).
  - **Acceptance:** PASS 4/4 pair cross-unit + cơ quan khác → ERR-DG-10 (TC-DG-27) + KH chưa `HOAN_THANH` → ERR-DG-11 (TC-DG-28).
  - **Cần có sẵn:** `[need: T-FR08-008 (✓ ≥1 KH HOAN_THANH)]`, `[need: ≥2 DON_VI cấp ĐP khác nhau (✗ chờ T-FR09-XXX STP-AG + STP-BG)]`
  - **Spec:** FR-VI-10 line 741, BR-VI-08-01 line 919

- 🟢 **T-FR08-010** FR-VI-10 — Mutation 403 API-layer (CRITICAL per review)
  - **Mô tả:** CB NV của `co_quan_duoc_danh_gia_id` cố PUT/PATCH/DELETE qua API direct (curl/Postman) trên 3 owned entity: `KE_HOACH_DANH_GIA`, `KET_QUA_DANH_GIA`, `BAO_CAO_DANH_GIA`. Memory `qa_htpldn_qtht_permission_bypass` cảnh báo BE có thể bypass khi role có Read.
  - **Acceptance:** 9 request (3 entity × 3 method) → 403 BE-layer, không chỉ UI hide button. Verify response body có error code permission.
  - **Cần có sẵn:** `[need: T-FR08-009 (✓ FR-VI-10 read OK)]`
  - **Spec:** FR-VI-10, TC-DG-29b

- 🟢 **T-FR08-011** Migration KH legacy `DOT_DANH_GIA` → `KE_HOACH_DANH_GIA`
  - **Mô tả:** Cover Open issue delta map §3 Finding 5 — KH cũ DB không có `co_quan_duoc_danh_gia_id`. Verify: (a) load form edit có default value backfill hay NULL; (b) save reject khi NULL (Required=Y line 1017); (c) FR-VI-10 behavior gì khi `co_quan_duoc_danh_gia_id=NULL` (defer Open issue).
  - **Acceptance:** TC-DG-41/42 PASS hoặc log bug data migration với SRS ref line 1017 + delta map §3 Finding 5.
  - **Cần có sẵn:** `[need: ≥1 KH legacy DOT_DANH_GIA pre-rename (✗ chờ T-INFRA-XXX DBA dump record từ DB cũ hoặc seed manual)]`
  - **Spec:** _DELTA-MAP-FR08.md §3 Finding 5 + §6 Open issue

- 🟢 **T-FR08-012** Migration rename reference cũ `dot-danh-gia` → `ke-hoach-danh-gia`
  - **Mô tả:** Grep code/API path/i18n string còn tồn tại reference cũ không. Test URL legacy `/dot-danh-gia/*` → 404 hoặc redirect. Verify FK `dot_danh_gia_id` rename `ke_hoach_danh_gia_id` 9 vị trí FR-VI-02..09 + SCR-VI-01.
  - **Acceptance:** 0 reference cũ trong code FE/BE + URL cũ redirect đúng (TC-DG-43).
  - **Cần có sẵn:** không
  - **Spec:** CHANGELOG-v3-to-v3.5.md line 880-1006, CR-10/A-ITEM-08

- 🟢 **T-FR08-013** Permission matrix 7 role × SCR-VI-01 + QTHT × FR-VI-10
  - **Mô tả:** Test TVV/CG/NHT/DN truy cập SCR-VI-01 → 403 (TC-DG-32/33/34). Test CB_NV_TW xem KH `don_vi_id=BN` → 403 (TC-DG-35, BR-AUTH-08 scope chỉ TW không phải all). Test QTHT × FR-VI-10 ngoại lệ BR-AUTH-03 (TC-DG-35a — review suggestion 2).
  - **Acceptance:** 5 TC negative PASS + 1 TC QTHT edge PASS.
  - **Cần có sẵn:** `[need: T-FR08-008 (✓ ≥1 KH HOAN_THANH)]`, `[need: TAI_KHOAN role TVV/CG/NHT/DN/QTHT (✓ users.csv default)]`
  - **Spec:** permission-matrix.md, BR-AUTH-03/08

- 🟢 **T-FR08-014** BR-NOTIF-01 verify 4 thời điểm channel + payload
  - **Mô tả:** Verify TB gửi đúng 4 thời điểm v3.5 (FR-VI-03 trình PC / FR-VI-04 duyệt PC / FR-VI-08 trình BC / FR-VI-09 duyệt BC) — recipient (CB NV creator + CB PD reviewer), channel (in-app/email), content fields. Delta map Finding 6 đánh dấu "ưu tiên test".
  - **Acceptance:** 4 TB record (verify in-app inbox + email queue) + content khớp template + retry logic nếu fail.
  - **Cần có sẵn:** `[need: T-FR08-003 (✓) → T-FR08-008 (✓ đủ 4 transition)]`
  - **Spec:** BR-NOTIF-01 line 1239-1243, delta map Finding 6

- 🟢 **T-FR08-015** Edge case calculation — trọng số tolerance + xếp loại boundary
  - **Mô tả:** TC-DG-08/21a/21b/36 — Σ trọng số 4 case boundary (99.99 / 100 / 100.01 / 100.02) + xếp loại 5 case (89.9/90/70/50/49.9). Formula `Σ(điểm × trọng số / 100)` với fixture cố định.
  - **Acceptance:** 9 sub-case PASS theo BR-CALC-04 + BR-VI-08-04.
  - **Cần có sẵn:** `[need: T-FR08-006 (✓ ≥1 KH BAO_CAO có KET_QUA_DANH_GIA)]`
  - **Spec:** BR-CALC-04, BR-VI-08-04

- 🟢 **T-FR08-016** HUY transition + guard lý do (4 state source + reject 2 state CB PD)
  - **Mô tả:** Test HUY từ 4 state source per SRS:1167 (LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO) → terminal HUY. Verify guard "Có lý do" (TC-DG-31a). HUY từ `HOAN_THANH`/`HUY` → reject. Defer SPEC-CLARIFY-FR08-06 cho 2 state CB PD `CHO_DUYET_PC` + `CHO_PHE_DUYET`.
  - **Acceptance:** 4 HUY PASS + reject thiếu lý do + reject từ terminal state.
  - **Cần có sẵn:** `[need: T-FR08-003 → T-FR08-007 đủ KH ở 4 state source]`
  - **Spec:** SRS line 1167 SM table, BR-VI-08-06

- 🟢 **T-FR08-017** Edge file_dinh_kem matrix 5 format × valid/invalid + multi-file
  - **Mô tả:** TC-DG-40 — 5 format (PDF/DOC/DOCX/XLS/XLSX) × valid/>20MB/sai format + multi-file (50 file concurrent, aggregate size, drag-drop reorder, replace, server timeout).
  - **Acceptance:** Matrix 15 sub-case + 4 multi-file edge sub-case PASS theo BR-VI-08-02.
  - **Cần có sẵn:** `[need: T-FR08-001 (✓ KH state LAP_KE_HOACH cho phép edit file)]`
  - **Spec:** BR-VI-08-02 line 1016

- 🚫 **T-FR08-018** BA escalate — 8 SPEC-CLARIFY pending
  - **Mô tả:** Escalate 8 SPEC-CLARIFY-FR08-01..08 cho BA — critical 3: (05) `tan_suat` DOT_XUAT enum vs BR-LEGAL-08 contradiction (block TC negative tần suất); (06) HUY guard 2 state CB PD; (07) hard-delete vs soft-delete contradiction; (08) `PHAN_CONG_DANH_GIA` entity schema.
  - **Acceptance:** BA confirm chính thức 8 question + update test-plan §2.1 / §2.5 / file 03/13.
  - **Cần có sẵn:** không (escalate first)
  - **Spec:** test-plan.md §Open issues line cuối

---

## Bảng tổng task

| Phase | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ | ❌ |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Seed + Workflow** (T-FR08-001..008) | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |
| **FR-VI-10 NEW v3.5** (T-FR08-009..010) | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Migration** (T-FR08-011..012) | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Permission + Edge + HUY** (T-FR08-013..017) | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| **BA escalate** (T-FR08-018) | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| **Tổng** | **18** | **17** | **0** | **0** | **0** | **1** | **0** | **0** |

---

## Cross-module dep summary

| Upstream module | State cần | Task ID dep |
|---|---|---|
| FR-05 (VV) | ≥3 VV `HOAN_THANH` + ≥1 `DA_DANH_GIA` scope `don_vi_id` user | T-FR08-005 |
| FR-09 (DON_VI) | ≥2 DON_VI cùng cấp + ≥1 cấp dưới (BTP-TW + STP-AG + STP-BG) | T-FR08-001, 009 |
| FR-10 (DM TC) | ≥1 set DM `TIEU_CHI_DG_HQ` ≥4 tiêu chí | T-FR08-002 |
| FR-12 (TAI_KHOAN) | ≥6 account CB_NV + CB_PD 3 cấp TW/BN/ĐP | T-FR08-001..004, 013 |

---

*Todo generated 2026-05-12 13:30:00 từ test-plan.md v1.1 (Revised) + review.md (12 gap + 10 suggestion). Áp dụng ≥80% feedback: 4 blocker + 8 important gap. 8 SPEC-CLARIFY escalate BA qua T-FR08-018.*
