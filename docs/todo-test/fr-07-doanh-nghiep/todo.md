# TODO — FR-07 — Doanh nghiệp

> File module test-plan: [test-plan.md](test-plan.md) (revised 2026-05-12 12:25:00, 45 TC).
> Review: [review.md](review.md) (REVISE, applied).
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream
>
> **Cross-module upstream chính:** FR-10 (DM TINH_THANH/LOAI_DN/LINH_VUC + DON_VI + FR-VIII-22 self-reg), FR-05 (VU_VIEC để test ERR-DN-03), FR-06 (chi trả công thức để test DN-045 quy_mo cascade).

---

## Tổng hợp

| Nhóm | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ | Task IDs |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| **Seed prerequisite** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | T-FR07-001, T-FR07-002 |
| **CRUD core (FR-V.III-01)** | 3 | 3 | 0 | 0 | 0 | 0 | 0 | T-FR07-003..005 |
| **Search (FR-V.III-02)** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | T-FR07-006..007 |
| **Cross-module** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | T-FR07-008..009 |
| **Permission matrix** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | T-FR07-010 |
| **Negative + edge** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | T-FR07-011..012 |
| **BA escalate** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | T-FR07-013 |
| **Tổng** | **13** | **13** | **0** | **0** | **0** | **0** | **0** | |

---

## Tasks

### Seed prerequisite

- 🟢 **T-FR07-001** Seed DM dùng chung cho FR-07 (TINH_THANH 63 + LOAI_DN ≥3 + LINH_VUC_KINH_DOANH ≥5)
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: DM LOAI_DN ≥3 record HOAT_DONG (✗ chưa seed — chờ T-FR10-006); DM LINH_VUC_KINH_DOANH ≥5 HOAT_DONG (✗ chờ T-FR10-007); DM TINH_THANH ≥63 (✗ — chờ T-FR10-XXX FR-VIII-30)]`

- 🟢 **T-FR07-002** Seed ≥6 DN self-reg HOAT_DONG (2 ĐP-AG / 2 BN / 2 TW) qua FR-VIII-22
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: DON_VI ≥7 record (✗ — chờ T-FR10-003); TAI_KHOAN flow self-reg FR-VIII-22 ready (✗ — chờ T-FR10-self-reg); T-FR07-001 ✅]`

### CRUD core (FR-V.III-01)

- 🟢 **T-FR07-003** TC DN-001..002 — Read list + chi tiết tab Thông tin cơ bản (28 component UI)
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥6 DN HOAT_DONG (✗ chờ T-FR07-002); verify SCR-V.III-02 component count theo line :323-354 SRS]`

- 🟢 **T-FR07-004** TC DN-003..005 — Update DN, AUDIT_LOG, auto-suggest quy_mo, WRN-DN-01 override
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥3 DN quy_mo distinct (✗ chờ T-FR07-002); endpoint /audit-logs hoặc DB query method confirm (⚠️ verify khi chạy)]`

- 🟢 **T-FR07-005** TC DN-006..012 — Delete soft + 4 tab (HSPL/Lịch sử HT/Chi trả/Multi-LV/email-no-OTP)
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥1 DN có VU_VIEC DANG_XU_LY (✗ chờ FR-05 seed VU_VIEC); ≥2 DN soft-delete sau test; tab HSPL needs ≥3 HO_SO_PHAP_LY_DN per DN (✗ chờ FR-12 seed)]`

### Search (FR-V.III-02)

- 🟢 **T-FR07-006** TC DN-013..017 — Search tu_khoa + filter quy_mo/tinh_thanh/linh_vuc multi-select
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥6 DN HOAT_DONG (✗ chờ T-FR07-002); DM TINH_THANH 63 + LINH_VUC ≥5 (✗ chờ T-FR07-001); SPEC-CLARIFY-FR07-04 AND/OR cho linh_vuc_ids[] (⚠️ BA confirm)]`

- 🟢 **T-FR07-007** TC DN-018..021 — Filter ngày HT + empty state INF-DN-TK-01 + sanitize >200 + pagination 20/page
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥21 DN để verify pagination page 2 (✗ chờ seed mở rộng); ≥1 DN có VU_VIEC trong khoảng [tu_ngay, den_ngay]]`

### Cross-module

- 🟢 **T-FR07-008** TC DN-024..026 — Dropdown DN ở FR-05/06/12 visible + scope BR-AUTH-08
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥6 DN HOAT_DONG đa scope ĐP/BN/TW (✗ chờ T-FR07-002); module FR-05/06/12 deploy ready với dropdown DN (⚠️ verify khi chạy)]`

- 🟢 **T-FR07-009** TC DN-045 — Cross-module quy_mo→FR-06 recompute (PENDING SPEC-CLARIFY-FR07-06)
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥1 DN quy_mo=NHO có VU_VIEC + HO_SO_CHI_TRA tồn tại (✗ chờ FR-05 + FR-06 seed); SPEC-CLARIFY-FR07-06 BA confirm cascade recompute hay snapshot (⚠️ BLOCKING)]`

### Permission matrix

- 🟢 **T-FR07-010** TC DN-027..033 — 11 role × 9 action + BR-AUTH-08 2-tier + verify [+Thêm mới]/[Import Excel] không có
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥6 DN đa scope (✗ chờ T-FR07-002); account cb_nv_tw/bn/dp/pd_tw/pd_dp/dn-self/nht_01 active (✗ chờ T-FR10 user seed); NHT row pending SPEC-CLARIFY-FR07-03]`

### Negative + edge

- 🟢 **T-FR07-011** TC DN-034..040 — ERR-DN-01..02 + CHECK negative + FK violation + optimistic lock + XSS
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥2 DN HOAT_DONG để test MST trùng + concurrent edit (✗ chờ T-FR07-002)]`

- 🟢 **T-FR07-012** TC DN-041..044 — Email format invalid + nguoi_dai_dien blank + tong_nguon_von/doanh_thu negative
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: ≥1 DN HOAT_DONG đầy đủ field để edit (✗ chờ T-FR07-002)]`

### BA escalate

- 🟢 **T-FR07-013** Escalate BA SPEC-CLARIFY-FR07-04/05/06 trước khi chạy DN-017/022/023/045
  - **Kết quả:** chưa chạy.
  - **Cần có sẵn:** `[need: BA có lịch confirm trong 24h (⚠️ phụ thuộc BA availability); 3 ticket SPEC-CLARIFY chuẩn bị câu hỏi rõ (✗ draft chờ)]`

---

## Note tracking

- 2026-05-12 12:25:00 — Todo tạo lần đầu sau revise test-plan.md v1.1. Tổng 13 task, 8 task có cross-module dep upstream FR-10 (DM + DON_VI + self-reg).
- Cross-module link tới FR-10: T-FR07-001 (DM TINH_THANH/LOAI_DN/LINH_VUC), T-FR07-002 (DON_VI + FR-VIII-22 self-reg).
- Cross-module link tới FR-05: T-FR07-005 (VU_VIEC DANG_XU_LY cho ERR-DN-03), T-FR07-009 (quy_mo cascade).
- Cross-module link tới FR-06: T-FR07-009 (chi trả công thức recompute).
- Cross-module link tới FR-12: T-FR07-005 (HO_SO_PHAP_LY_DN cho tab HSPL).
- 3 SPEC-CLARIFY mới (04/05/06) — block 4 TC (DN-017/022/023/045), task T-FR07-013 escalate BA.
