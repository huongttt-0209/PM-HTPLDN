# TODO — FR-05 — Vụ việc TGPL (CORE)

> **Module:** FR-V.I-01..17 + NEW-01/02/05 + CROSS-01 (SCR-V.I-01..05) — ⭐ CORE entity nhất hệ thống
> **Test plan:** [test-plan.md](test-plan.md) (v1.1, revised 2026-05-12 13:00:00)
> **State machine:** 12 state + 21 transition + 3 self-loop (SL1/SL2/SL3 công khai)
> **Tổng TC:** ~135 (±10%) — 33 Happy + 63 Negative + 39 Edge
> **Generated:** 2026-05-12 13:00:00

## Icon meaning

- ✅ Đạt | ⚠️ Sai spec | ❌ Lỗi | 🚫 Không test được | ⏭ Hoãn | 🤷 Không xác định
- ⏳ Chờ upstream (icon mặc định khi tạo) | 🟢 Sẵn sàng chạy (dep state thoả)

---

## Tracker — Active task list

### Nhóm 1 — SPEC-CLARIFY tickets (BA confirm trước R1)

- 🟢 **T-FR05-001** Hỏi BA SC-01 soft-delete vs hard-delete VU_VIEC
  - **Kết quả:** Pending BA reply. Block TC-DELETE-01/02 + TC25-E4. [test-plan §SPEC-CLARIFY]
  - **Cần có sẵn:** Không (action BA, không phải dep state)
- 🟢 **T-FR05-002** Hỏi BA SC-02 BR-AUTH-10 áp dụng FR-05 hay đã OUT
  - **Kết quả:** Pending. Block TC-NHT-01..03 (UC60 lọc kép). [test-plan §SPEC-CLARIFY]
- 🟢 **T-FR05-003** Hỏi BA SC-03 behavior 3 placeholder transition T15/T21/T12
  - **Kết quả:** Pending. Block TC-PLACEHOLDER-01..03. [test-plan §SPEC-CLARIFY]
- 🟢 **T-FR05-004** Hỏi BA SC-04 UC106 checklist versioning + SC-05 NĐ55 Đ.8 K.1 SLA 15 ngày + SC-06 DN auth QA env
  - **Kết quả:** Pending. Block TC-KT-04, TC-SLA-04, mọi DN TC. [test-plan §SPEC-CLARIFY]

### Nhóm 2 — Seed pre-check upstream

- ⏳ **T-FR05-005** Verify seed DN HOAT_DONG ≥3 record (cross FR-07)
  - **Kết quả:** ⏳ Chờ T-FR07-XXX. [seed-checklist-fr-05.md]
  - **Cần có sẵn:** [need: ≥3 DN HOAT_DONG đủ field BR-CALC-04 (la_nu_lam_chu, so_lao_dong_nu, so_lao_dong_khuyet_tat) (✗ chờ T-FR07-XXX); verify `?trang_thai=HOAT_DONG&don_vi_id=HN` ≥1, `?don_vi_id=BG` ≥1]
- ⏳ **T-FR05-006** Verify seed TVV + CG + NHT HOAT_DONG (cross FR-04)
  - **Kết quả:** ⏳ Chờ T-FR04-XXX advance-state. [seed-checklist-fr-05.md]
  - **Cần có sẵn:** [need: ≥3 TVV HOAT_DONG mỗi LV cần test, ≥1 CG HOAT_DONG, ≥1 NHT HOAT_DONG mỗi cấp ĐP (✗ chờ T-FR04-XXX); verify `?loai_tvv=TVV&trang_thai=HOAT_DONG&linh_vuc_id=X` mỗi LV ≥1]
- ⏳ **T-FR05-007** Verify seed DM LINH_VUC_PL ≥6 + HO_SO_DE_NGHI_HT (cross FR-10)
  - **Kết quả:** ⏳ Chờ T-FR10-XXX. [seed-checklist-fr-05.md]
  - **Cần có sẵn:** [need: DM LINH_VUC_PL ≥6 record HOAT_DONG; DM HO_SO_DE_NGHI_HT 6 hạng mục UC106 (✗ chờ T-FR10-XXX); verify `?loai_dm=LINH_VUC_PL` ≥6, `?loai_dm=HO_SO_DE_NGHI_HT` =6]
- ⏳ **T-FR05-008** Verify seed BM (Biểu mẫu) ≥3 CONG_KHAI (cross FR-09)
  - **Kết quả:** ⏳ Chờ T-FR09-XXX. [seed-checklist-fr-05.md]
  - **Cần có sẵn:** [need: ≥3 BM trạng thái CONG_KHAI cho mẫu HSCT/KQ (✗ chờ T-FR09-XXX); verify `?trang_thai=CONG_KHAI` ≥3]
- ⏳ **T-FR05-009** Verify seed TO_CHUC_TU_VAN HOAT_DONG (≥2 TVV thuộc tổ chức)
  - **Kết quả:** ⏳ Chờ T-FR04-XXX. [seed-checklist-fr-05.md]
  - **Cần có sẵn:** [need: ≥1 TO_CHUC_TU_VAN HOAT_DONG có ≥2 TVV thuộc tổ chức (✗ chờ T-FR04-XXX); verify `TO_CHUC?trang_thai=HOAT_DONG` ≥1]
- ⏳ **T-FR05-010** Seed CAU_HINH_SLA bo_sung_timeout = 5 ngày LV + CAU_HINH_QUY_TRINH version active (cross FR-10)
  - **Kết quả:** ⏳ Chờ T-FR10-XXX. [seed-checklist-fr-05.md]
  - **Cần có sẵn:** [need: CAU_HINH_SLA `bo_sung_timeout=5` ngày LV; CAU_HINH_QUY_TRINH 1 version `is_active=1` (✗ chờ T-FR10-XXX); verify `?key=bo_sung_timeout` =5]

### Nhóm 3 — State lifecycle 12 state (workflow tests)

- ⏳ **T-FR05-011** Workflow nhánh 1: UC54 nhập tay → T04 → DA_TIEP_NHAN → T06 → DANG_KIEM_TRA → T07 → DA_PHAN_CONG → T13 → DANG_XU_LY → T16 → CHO_PHE_DUYET → T17 → DA_DUYET → T19 → HOAN_THANH → T20 → DA_DANH_GIA
  - **Kết quả:** ⏳ Chờ seed upstream. [workflow-test-report-fr-05.md]
  - **Cần có sẵn:** [need: T-FR05-005..010 đủ state HOAT_DONG; ≥1 CB_NV_TW + ≥1 CB_PD_TW + ≥1 NHT login OK]
- ⏳ **T-FR05-012** Workflow nhánh 2: UC52 DN gửi HS → T03 → CHO_TIEP_NHAN → T05 → DA_TIEP_NHAN → ... → DA_DUYET
  - **Kết quả:** ⏳ Chờ SC-06 (DN auth). [workflow-test-report-fr-05.md]
  - **Cần có sẵn:** [need: SC-06 confirmed DN auth method (✗ chờ T-FR05-004); ≥3 DN HOAT_DONG (✗ chờ T-FR05-005)]
- ⏳ **T-FR05-013** Workflow nhánh 3 YEU_CAU_BO_SUNG: DANG_KIEM_TRA → T08 → YEU_CAU_BO_SUNG → T10 → DANG_KIEM_TRA (3 lần) → T12 → TU_CHOI auto
  - **Kết quả:** ⏳ Chờ seed + SC-06. [workflow-test-report-fr-05.md]
  - **Cần có sẵn:** [need: ≥1 DN HOAT_DONG, ≥1 VV trạng thái DANG_KIEM_TRA (✗ chờ T-FR05-011 happy path); SC-06 (✗ chờ T-FR05-004)]
- ⏳ **T-FR05-014** Workflow nhánh 4: SL1 Công khai DA_DUYET → CB PD click [Công khai] → state DA_DUYET giữ + cong_khai=1
  - **Kết quả:** ⏳ Chờ seed + env mock Cổng PLQG. [workflow-test-report-fr-05.md]
  - **Cần có sẵn:** [need: ≥1 VV DA_DUYET (✗ chờ T-FR05-011); mock API Cổng PLQG hoạt động hoặc intercept qua MCP `list_network_requests`]

### Nhóm 4 — UC106 checklist 6 hạng mục

- ⏳ **T-FR05-015** UC56 kiểm tra HS — 6 hạng mục UC106 (Mẫu 01 NĐ55, ĐKKD, Quy mô DN, HĐ TV, VB TV đầy đủ, VB TV loại BMKD)
  - **Kết quả:** ⏳ Chờ seed DM HO_SO_DE_NGHI_HT. [06-TC-kiem-tra.md]
  - **Cần có sẵn:** [need: DM HO_SO_DE_NGHI_HT = 6 hạng mục từ UC106 config (✗ chờ T-FR05-007); ≥1 VV DANG_KIEM_TRA (✗ chờ T-FR05-011)]
- ⏳ **T-FR05-016** BR-EC-15 — counter YCBS 1/2/3 highlight đỏ ≥2, auto TU_CHOI lần 4
  - **Kết quả:** ⏳ Chờ T-FR05-013 nhánh YCBS. [06-TC-kiem-tra.md]
  - **Cần có sẵn:** [need: VV YEU_CAU_BO_SUNG counter `bo_sung_count=2` (✗ chờ T-FR05-013 mid-state)]

### Nhóm 5 — Phân công TVV/NHT (UC59 modal 2 thẻ + BR-CALC-04 + BR-AUTH-10)

- ⏳ **T-FR05-017** UC59 modal 2 thẻ Cá nhân/Tổ chức + BR-CALC-04 priority (4 yếu tố)
  - **Kết quả:** ⏳ Chờ seed TVV + TO_CHUC. [09-TC-phan-cong.md]
  - **Cần có sẵn:** [need: ≥3 TVV HOAT_DONG mỗi LV (✗ chờ T-FR05-006); ≥1 TO_CHUC HOAT_DONG có ≥2 TVV (✗ chờ T-FR05-009)]
- ⏳ **T-FR05-018** BR-AUTH-10 lọc kép — NHT chỉ thấy VV được phân công đích danh (BLOCKED chờ SC-02)
  - **Kết quả:** 🚫 Chờ BA SC-02. [10-TC-xac-nhan.md]
  - **Cần có sẵn:** [need: SC-02 confirmed BR-AUTH-10 áp dụng FR-05 hay OUT (✗ chờ T-FR05-002)]
- ⏳ **T-FR05-019** UC60 NHT/TVV/CG xác nhận/từ chối phân công (T13 + T14)
  - **Kết quả:** ⏳ Chờ T-FR05-017 → VV DA_PHAN_CONG. [10-TC-xac-nhan.md]
  - **Cần có sẵn:** [need: ≥1 VV DA_PHAN_CONG với người phân công sẵn login (✗ chờ T-FR05-017)]

### Nhóm 6 — DN bổ sung HS (UC NEW-02) — 3 lần + quá hạn

- ⏳ **T-FR05-020** UC NEW-02 DN bổ sung HS T10 — 3 lần BR-EC-15 + auto TU_CHOI lần 4
  - **Kết quả:** ⏳ Chờ SC-06 + seed. [19-TC-dn-bo-sung.md]
  - **Cần có sẵn:** [need: SC-06 confirmed (✗ chờ T-FR05-004); ≥1 VV YEU_CAU_BO_SUNG (✗ chờ T-FR05-013)]
- ⏳ **T-FR05-021** BR-EC-16 quá hạn bổ sung auto-reject (T11 scheduled job)
  - **Kết quả:** ⏳ Chờ T-FR05-010 cấu hình SLA + scheduled job deploy. [19-TC-dn-bo-sung.md, 21-TC-sla-cross.md]
  - **Cần có sẵn:** [need: CAU_HINH_SLA `bo_sung_timeout=5` (✗ chờ T-FR05-010); scheduled job CROSS-01 deploy verified]

### Nhóm 7 — Công khai VV (FR-V.I-NEW-05) — SL1/SL2/SL3

- ⏳ **T-FR05-022** SL1/SL2 Công khai VV DA_DUYET/HOAN_THANH + BR-PUBLIC-04 whitelist 9 fields + BR-EC-20
  - **Kết quả:** ⏳ Chờ mock Cổng PLQG. [20-TC-cong-khai.md]
  - **Cần có sẵn:** [need: ≥2 VV DA_DUYET + ≥2 VV HOAN_THANH cong_khai=0 (✗ chờ T-FR05-011); mock API Cổng PLQG hoặc env LGSP sandbox]
- ⏳ **T-FR05-023** SL3 Hủy công khai + ly_do_huy ≥20 ký tự (ERR-CK-VV-10)
  - **Kết quả:** ⏳ Chờ T-FR05-022. [20-TC-cong-khai.md]
  - **Cần có sẵn:** [need: ≥1 VV cong_khai=1 (✗ chờ T-FR05-022 happy path)]

### Nhóm 8 — Migration data `nguoi_ho_tro_id` → 3 cột mới (TC25 — 8 TC)

- 🟢 **T-FR05-024** Migration script verify backfill `loai_doi_tuong_xu_ly + nguoi_xu_ly_id` (TC25-H1)
  - **Kết quả:** Pending. Cần coordinate DBA. [25-TC-data-migration.md]
  - **Cần có sẵn:** [need: dump DB pre-migration có ≥3 VV `nguoi_ho_tro_id IS NOT NULL`; migration script DBA-provided]
- 🟢 **T-FR05-025** Migration negative + edge TC25-N1/N2/N3 + E1/E2/E3 (FE chi tiết, FR-11 báo cáo, audit, rollback, idempotent)
  - **Kết quả:** Pending T-FR05-024. [25-TC-data-migration.md]
  - **Cần có sẵn:** [need: T-FR05-024 chạy xong; FR-11 báo cáo "VV theo người xử lý" deployed]
- 🟢 **T-FR05-026** Migration edge TC25-E4 soft vs hard delete cho VV migrated (BLOCKED SC-01)
  - **Kết quả:** 🚫 Chờ BA SC-01. [25-TC-data-migration.md]
  - **Cần có sẵn:** [need: SC-01 confirmed (✗ chờ T-FR05-001)]

### Nhóm 9 — Permission matrix + cross-unit isolation

- ⏳ **T-FR05-027** Permission matrix 11 role × 17 action — TC-PERM-01..12 + TC-AUTH-01..05
  - **Kết quả:** ⏳ Chờ seed + login OK 11 role. [22-TC-perm-cross-unit.md, 23-TC-perm-role.md]
  - **Cần có sẵn:** [need: 11 role login OK (`qtht_01`, `cb_nv_tw_01`, `cb_nv_bn_01`, `cb_nv_dp_01`, `cb_pd_tw_01`, `cb_pd_bn_01`, `cb_pd_dp_01`, `nht_01`, TVV + CG seed (✗ chờ T-FR05-006), DN auth (✗ chờ SC-06)); ≥1 VV per cấp test]
- ⏳ **T-FR05-028** BR-FLOW-03 lock đã duyệt + QTHT force-edit + audit `is_force_edit=true` (TC-LOCK-01..03)
  - **Kết quả:** ⏳ Chờ VV DA_DUYET. [07-TC-chi-tiet.md]
  - **Cần có sẵn:** [need: ≥1 VV DA_DUYET + ≥1 VV HOAN_THANH (✗ chờ T-FR05-011)]

### Nhóm 10 — Cross-module impact smoke

- ⏳ **T-FR05-029** Cross-module smoke FR-06/FR-08/FR-11/FR-14/FR-IV-CROSS-01 — 5 smoke TC
  - **Kết quả:** ⏳ Chờ FR-05 PASS R1 P0 ≥80%. [test-plan §8]
  - **Cần có sẵn:** [need: FR-05 P0 ≥80% PASS R1 (✗ chờ T-FR05-011..028); FR-06/08/11/14 môi trường deployed]

### Nhóm 11 — Edge case 18+ transition + 3 placeholder

- ⏳ **T-FR05-030** TC-PLACEHOLDER-01..03 — T15 auto-return NHT timeout + T21 mở lại từ TU_CHOI + T12 auto 3 lần (BLOCKED SC-03)
  - **Kết quả:** 🚫 Chờ BA SC-03. [21-TC-sla-cross.md, 25-TC-data-migration.md, 06-TC-kiem-tra.md]
  - **Cần có sẵn:** [need: SC-03 confirmed behavior 3 placeholder (✗ chờ T-FR05-003)]

---

## Module bị block

| Block ID | Mô tả | Owner | ETA unblock |
|---|---|:-:|:-:|
| SC-01 | Soft vs hard delete cho VU_VIEC | BA | TBD |
| SC-02 | BR-AUTH-10 áp dụng FR-05? | BA | TBD |
| SC-03 | 3 placeholder transition behavior | BA | TBD |
| SC-04 | UC106 checklist versioning | BA | TBD |
| SC-05 | NĐ55 Đ.8 K.1 SLA 15 ngày — web-verify | BA + Pháp chế | TBD |
| SC-06 | DN auth Tier 2 VNeID trên QA env | BA + DevOps | TBD |
| Upstream T-FR04 | TVV/CG/NHT seed HOAT_DONG | QA FR-04 | TBD |
| Upstream T-FR07 | DN HOAT_DONG seed | QA FR-07 | TBD |
| Upstream T-FR09 | BM CONG_KHAI seed | QA FR-09 | TBD |
| Upstream T-FR10 | DM + CAU_HINH seed | QA FR-10 | TBD |
| Env mock Cổng PLQG | Mock API hoặc sandbox LGSP | Infra/DevOps | TBD |

---

## Tiến độ

| Trạng thái | Count |
|---|---:|
| ✅ Đạt | 0 |
| ⚠️ Sai spec | 0 |
| ❌ Lỗi | 0 |
| 🚫 Không test được | 3 (T-FR05-018, 026, 030) |
| ⏳ Chờ upstream | 23 |
| 🟢 Sẵn sàng | 7 (T-FR05-001..004, 024, 025) |
| **Tổng** | **30** |

---

*Generated 2026-05-12 13:00:00 from test-plan.md v1.1. Module XL — CORE entity nhất hệ thống. Cross-module dep cần T-FR04/07/09/10 PASS upstream + 6 BA SPEC-CLARIFY tickets unblock trước R1.*
