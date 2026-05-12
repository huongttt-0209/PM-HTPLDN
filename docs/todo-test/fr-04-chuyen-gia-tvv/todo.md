# TODO — FR-04 — CG/TVV/NHT/TC-TV

> Module XL complex — 4 entity (TU_VAN_VIEN + NGUOI_HO_TRO + TO_CHUC_TU_VAN + DANH_GIA_SAU_VU_VIEC), 3 SM, 9 SCR, 83 TC.
>
> **Tham chiếu shared:** [`test-plan.md`](test-plan.md) · [`review.md`](review.md) · [`../../../tasks/state-snapshot.md`](../../../tasks/state-snapshot.md)
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream
>
> **Quy ước Task ID:** `T-FR04-XXX` (XXX = 001..NNN).
> **Cross-module upstream:** seed danh mục (LINH_VUC_PL, DON_VI) + role TAI_KHOAN từ FR-10. Lifecycle SM mở rộng cho TCTV + NHT — phải walk workflow theo `flow-module.md` §FR-04.

---

## Icon column meaning

| Icon | Nghĩa |
|:-:|---|
| 🟢 | Sẵn sàng chạy — mọi dep `(✓ N)` |
| 🔵 | Đang chạy |
| ✅ | PASS clean |
| ⚠️ | Sai spec / partial |
| 🚫 | Block — chờ dev fix hoặc BA confirm |
| ⏳ | Chờ upstream task / state entity khác |
| ❌ | FAIL — bug confirmed |

---

## Tasks

### Group 1 — Seed entity baseline (Tier 1-2)

- 🟢 **T-FR04-001** Seed CG baseline — 6 record `loai_tvv='CG'` cover 6 LV (DN/TM/LĐ/Thuế/SHTT/Đất đai), state `HOAT_DONG`
  - **Cần có sẵn:** [need: DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001); DM DON_VI ≥3 TW/BN/ĐP (✗ chờ T-FR10-002); TAI_KHOAN ≥6 user role CG (✗ chờ T-FR10-003)]
  - **Kết quả:** _chưa chạy_
  - **Output:** `seed-checklist-fr04-001-cg-baseline.md`

- 🟢 **T-FR04-002** Seed TVV baseline — 6 record `loai_tvv='TVV'` cover 6 LV × 3 cấp (TW/BN/ĐP), state `HOAT_DONG`
  - **Cần có sẵn:** [need: DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001); DON_VI ≥7 (TW + 3 BN + 3 ĐP) (✗ chờ T-FR10-002); TAI_KHOAN ≥6 user role TVV (✗ chờ T-FR10-003)]
  - **Kết quả:** _chưa chạy_

- 🟢 **T-FR04-003** Seed NHT — workflow tạo 6 NHT qua SCR-IV-NHT-02 (QTHT/CB NV), state `CHO_KICH_HOAT`
  - **Cần có sẵn:** [need: DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001); DON_VI ≥6 (BTP-TW + 3 BN + 2 ĐP) (✗ chờ T-FR10-002); VAI_TRO 'NHT' (✗ chờ T-FR10-003)]
  - **Kết quả:** _chưa chạy — 6 NHT mới (BR-FLOW-NHT-01 bỏ thẩm định)._

- 🟢 **T-FR04-004** Advance NHT state — click mail kích hoạt + set MK lần đầu (FR-VIII-15) → 6 NHT `HOAT_DONG`
  - **Cần có sẵn:** [need: ≥6 NHT state `CHO_KICH_HOAT` (✗ chờ T-FR04-003); MailHog inbox accessible (✓ http://103.172.236.130:8025)]
  - **Kết quả:** _chưa chạy — verify dropdown FR-05/FR-02 đọc được NHT._

- 🟢 **T-FR04-005** Seed TCTV — workflow tạo 6 TCTV (CONG_TY_LUAT/VP_LUAT_SU/TT_TVPL/KHAC) cover 3 cấp, state `MOI_DANG_KY`
  - **Cần có sẵn:** [need: DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001); DON_VI ≥6 (✗ chờ T-FR10-002)]
  - **Kết quả:** _chưa chạy — 6 record start lifecycle SM-TCTV._

- 🟢 **T-FR04-006** Advance TCTV state lifecycle — `MOI_DANG_KY` → `CHO_PHE_DUYET` → `HOAT_DONG` (FR-IV-NEW-04 + NĐ 55/2019 Đ.9)
  - **Cần có sẵn:** [need: ≥6 TCTV state `MOI_DANG_KY` (✗ chờ T-FR04-005); CB PD account `cb_pd_tw_01` + `cb_pd_bn_01` + `cb_pd_dp_01` (✓ users.csv)]
  - **Kết quả:** _chưa chạy — verify badge "Hoạt động" + so_quyet_dinh field._

### Group 2 — Functional CRUD per entity (Group A FULL test)

- 🟢 **T-FR04-007** TC 01 — TVV/CG CRUD + Search functional (9 TC: 2H + 4N + 3E, FR-IV-01/02)
  - **Cần có sẵn:** [need: ≥6 TVV + ≥6 CG state `HOAT_DONG` (✗ chờ T-FR04-001 + T-FR04-002); QTHT + CB NV cấp TW/BN/ĐP (✓ users.csv)]
  - **Kết quả:** _chưa chạy — bao gồm E1 migration probe `loai_tvv='NHT'`._
  - **Output:** `functional-test-report-fr04-007-tvv-cg-crud.md`

- 🟢 **T-FR04-008** TC 02 — NHT submit hồ sơ + cập nhật năng lực TVV/CG (5 TC, FR-IV-03/04)
  - **Cần có sẵn:** [need: ≥6 NHT state `HOAT_DONG` (✗ chờ T-FR04-004); TVV pool có ≥3 state `MOI_DANG_KY` (✗ chờ T-FR04-014)]
  - **Kết quả:** _chưa chạy._

- 🟢 **T-FR04-009** TC 03 — Chi tiết TVV/CG 5 tab (4 TC, FR-IV-05/10/11)
  - **Cần có sẵn:** [need: ≥1 TVV `HOAT_DONG` có lịch sử VV + đánh giá (✗ chờ T-FR04-002 + T-FR04-019)]
  - **Kết quả:** _chưa chạy._

- 🟢 **T-FR04-010** TC 04 — Thẩm định 4 nhóm tiêu chí + tiếp nhận (5 TC, FR-IV-06/13)
  - **Cần có sẵn:** [need: ≥3 TVV state `CHO_THAM_DINH` (✗ chờ T-FR04-014); CB NV cấp TW/BN/ĐP (✓ users.csv)]
  - **Kết quả:** _chưa chạy — guard BR-FLOW-03 sau gửi KQ._

- 🟢 **T-FR04-011** TC 05 — CB PD phê duyệt → `CHO_KICH_HOAT` + auto-cấp TK (5 TC, FR-IV-07 + FR-VIII-15)
  - **Cần có sẵn:** [need: ≥3 TVV state `CHO_PHE_DUYET` (✗ chờ T-FR04-010); CB PD `cb_pd_tw_01/bn/dp` (✓ users.csv)]
  - **Kết quả:** _chưa chạy — verify auto-cấp TK + mail kích hoạt FR-VIII-15._

- 🟢 **T-FR04-012** TC 06 — Công khai MLTV TVV + TCTV lên Cổng PLQG (4 TC, FR-IV-08 + BR-PUBLIC-01..03)
  - **Cần có sẵn:** [need: ≥3 TVV `CHO_KICH_HOAT/HOAT_DONG` (✗ chờ T-FR04-011); ≥3 TCTV `HOAT_DONG` (✗ chờ T-FR04-006); mock API Cổng PLQG 500 (env support)]
  - **Kết quả:** _chưa chạy — retry 3 lần + WRN-TCTV-04._

- 🟢 **T-FR04-013** TC 07 — Đánh giá DN → TVV + tổng hợp 1-5 (4 TC, FR-IV-09 + FR-IV-CROSS-01 + BR-CALC-06)
  - **Cần có sẵn:** [need: ≥3 TVV `HOAT_DONG` có ≥3 VV `HOAN_THANH` (✗ chờ T-FR05-XXX); DN account `9999999990/91` (✓ users.csv)]
  - **Kết quả:** _chưa chạy — verify `diem_danh_gia_tb` thang 1.0-5.0 + INF-TVV-DG-01._

- 🟢 **T-FR04-014** TC 04 + lifecycle setup — walk SM-TVV `MOI_DANG_KY → CHO_THAM_DINH → CHO_PHE_DUYET` để chuẩn bị pool cho TC04/05
  - **Cần có sẵn:** [need: NHT account `nht_01/02` + CB NV `cb_nv_tw/bn/dp_01` (✓ users.csv)]
  - **Kết quả:** _chưa chạy — seed pool 9 TVV mỗi state (3/TW + 3/BN + 3/ĐP)._

- 🟢 **T-FR04-015** TC 08 — TVV state update (TAM_DUNG/VO_HIEU_HOA/khôi phục) (4 TC, FR-IV-12)
  - **Cần có sẵn:** [need: ≥3 TVV `HOAT_DONG` không có VV pending (✗ chờ T-FR04-002 + T-FR04-011); guard ERR-TT-02]
  - **Kết quả:** _chưa chạy._

### Group 3 — TCTV functional + lifecycle (entity mới)

- 🟢 **T-FR04-016** TC 09 — TCTV CRUD + E2 DN view public Cổng PLQG (6 TC, FR-IV-NEW-01 + BR-LEGAL-09)
  - **Cần có sẵn:** [need: ≥6 TCTV trạng thái mixed (✗ chờ T-FR04-005 + T-FR04-006); DN `9999999990` (✓ users.csv)]
  - **Kết quả:** _chưa chạy._

- 🟢 **T-FR04-017** TC 10 + TC 11 — TCTV state update + phê duyệt (10 TC, FR-IV-NEW-02/04)
  - **Cần có sẵn:** [need: ≥3 TCTV `CHO_PHE_DUYET` + ≥3 `TU_CHOI` (✗ chờ T-FR04-005); CB PD cấp 3 (✓ users.csv)]
  - **Kết quả:** _chưa chạy — TC mới TU_CHOI→CHO_PHE_DUYET guard `updated_at`._

### Group 4 — NHT functional (entity mới)

- 🟢 **T-FR04-018** TC 12 + TC 13 — NHT CRUD + search + detail (8 TC, FR-IV-NHT-01/02/03)
  - **Cần có sẵn:** [need: ≥6 NHT `HOAT_DONG` (✗ chờ T-FR04-004); QTHT + CB NV cấp 3 (✓ users.csv)]
  - **Kết quả:** _chưa chạy — form 5 field, không upload, không thẩm định._

### Group 5 — Permission + cross-module

- 🟢 **T-FR04-019** TC 14 — Permission cross-role BR-AUTH-05/08/10 (11 TC: probe API + 3 actor lọc kép)
  - **Cần có sẵn:** [need: ≥3 TVV + ≥3 NHT + ≥3 TCTV mỗi cấp TW/BN/ĐP (✗ chờ T-FR04-001..006); 11 role accounts (✓ users.csv); CG `huongcg` (✓)]
  - **Kết quả:** _chưa chạy — bao gồm TC.P0-PROBE-API memory `qtht_permission_bypass` + N6 NHT + N7 TVV + N8 CG._
  - **Output:** `functional-test-report-fr04-019-permission.md`

- 🟢 **T-FR04-020** TC 15 — Cross-module impact 8 consumer (FR-05/12/14/03/02/11/01/16) dropdown + KPI + API public
  - **Cần có sẵn:** [need: ≥3 TVV + ≥3 CG + ≥3 NHT + ≥3 TCTV state `HOAT_DONG` (✗ chờ T-FR04-001..006); module consumer deployed (✗ chờ T-FR05/12/14/03/02/11/01/16 endpoint)]
  - **Kết quả:** _chưa chạy — verify enum rename `DANG_HOAT_DONG`→`HOAT_DONG` không break consumer._
  - **Output:** `functional-test-report-fr04-020-cross-module.md`

### Group 6 — Migration + edge regression

- 🟢 **T-FR04-021** Probe migration data cũ — query DB record cũ `loai_tvv='NHT'` (nếu còn) → verify FE crash / 500 / silent skip → log `SPEC-MIGRATION-IV-01`
  - **Cần có sẵn:** [need: DB access query `SELECT * FROM TU_VAN_VIEN WHERE loai_tvv='NHT'` (✗ chờ DBA grant); test environment DB snapshot v3.0 (✗ chờ infra)]
  - **Kết quả:** _chưa chạy — TC E1 file 01-TC-tvv-cg-crud.md._
  - **Output:** `bug-report-fr04-021-migration-loai-tvv-nht.md`

---

## Phụ thuộc cross-module (state-explicit)

| Upstream module | State cần | Task FR-04 phụ thuộc |
|---|---|---|
| FR-10 Quản trị HT | DM LINH_VUC_PL ≥6 record `HOAT_DONG` | T-FR04-001/002/003/005 |
| FR-10 Quản trị HT | DON_VI ≥7 (TW + 3 BN + 3 ĐP) `HOAT_DONG` | T-FR04-001..006 |
| FR-10 Quản trị HT | TAI_KHOAN + VAI_TRO 'TVV'/'CG'/'NHT' ≥6 mỗi role | T-FR04-001/002/003 |
| FR-10 Quản trị HT | MailHog `/api/v2/messages` reachable | T-FR04-004 + T-FR04-011 |
| FR-05 Vụ việc | ≥3 VV `HOAN_THANH` có TVV liên kết | T-FR04-013 |
| FR-05/12/14/03/02/11/01/16 | Endpoint deployed (dropdown / KPI / API public) | T-FR04-020 |
| Infra/DBA | DB query access + snapshot v3.0 | T-FR04-021 |

---

*TODO generated 2026-05-12 15:08:00 by Reviser/Todo writer — 21 task tổng (6 seed + 9 functional + 2 NHT/TCTV mới + 2 permission/cross + 1 migration + 1 lifecycle pool). Mọi task icon 🟢, Kết quả ≤25 từ, dep state-explicit theo CLAUDE.md memory `feedback_dependency_chain_state_explicit`.*
