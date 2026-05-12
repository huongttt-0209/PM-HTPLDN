# TODO — FR-09 — Biểu mẫu

> Generated 2026-05-12 12:55:00 từ [`test-plan.md`](test-plan.md) v1.1 (60 TC, 10 file TC `01-10`).
>
> **Tham chiếu shared:** [`../../../tasks/state-snapshot.md`](../../../tasks/state-snapshot.md) · [`test-plan.md`](test-plan.md) · [`review.md`](review.md)
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream
>
> **Task IDs:** T-FR09-001 → T-FR09-013

---

## Tổng hợp module

| Phase | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ | ❌ |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Seed** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **CRUD core** | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Lifecycle SM** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **CR-01 4 trường công khai** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Upload / Edge** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Permission** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **API outbound + Regression** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Tổng** | **13** | **13** | **0** | **0** | **0** | **0** | **0** | **0** |

---

## Tasks

### Seed

- 🟢 **T-FR09-001** Seed THU_MUC_BIEU_MAU 6 LV × 2 trạng thái (NHAP/CONG_KHAI) <a id="t-fr09-001"></a>
  - **Kết quả:** Chưa chạy. Mục tiêu ≥6 TM phủ 6 LV × 2 state.
  - **Cần có sẵn:** `[need: DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001)]`

- 🟢 **T-FR09-002** Seed BIEU_MAU 3-6 LV × 2 trạng thái + 4 trường công khai CR-01 <a id="t-fr09-002"></a>
  - **Kết quả:** Chưa chạy. Mục tiêu ≥12 BM, ≥3 BM có `cong_khai=1` + 4 trường công khai full.
  - **Cần có sẵn:** `[need: ≥6 THU_MUC_BIEU_MAU (✗ chờ T-FR09-001)]`

### CRUD core

- 🟢 **T-FR09-003** CRUD THU_MUC (TM-001..006) + negative ERR-TM-01..04 <a id="t-fr09-003"></a>
  - **Kết quả:** Chưa chạy. 6 TC ([`01-TC-thu-muc-crud.md`](01-TC-thu-muc-crud.md)).
  - **Cần có sẵn:** `[need: ≥6 LINH_VUC_PL + ≥1 CB_NV_TW account active (✗ chờ T-FR10-001)]`

- 🟢 **T-FR09-004** CRUD BIEU_MAU core (BM-001..010) + upload file doc/docx/xls/xlsx + ERR-BM-01..05 + optimistic lock <a id="t-fr09-004"></a>
  - **Kết quả:** Chưa chạy. 10 TC ([`04-TC-bieu-mau-crud.md`](04-TC-bieu-mau-crud.md)).
  - **Cần có sẵn:** `[need: ≥6 THU_MUC_BIEU_MAU state NHAP (✗ chờ T-FR09-001)]`

- 🟢 **T-FR09-005** Search TM + BM (TM-007..009, BM-011..013) + BR-EC-13 sanitize <a id="t-fr09-005"></a>
  - **Kết quả:** Chưa chạy. 6 TC ([`02-TC-thu-muc-search.md`](02-TC-thu-muc-search.md), [`06-TC-bieu-mau-search.md`](06-TC-bieu-mau-search.md)).
  - **Cần có sẵn:** `[need: ≥5 TM + ≥10 BM phủ ≥3 LV (✗ chờ T-FR09-002)]`

### Lifecycle State Machine

- 🟢 **T-FR09-006** Lifecycle TM/BM: NHAP → CONG_KHAI → AN → XOA (TM-010..013) + ERR-CK-01..02 + WRN-CK-01 <a id="t-fr09-006"></a>
  - **Kết quả:** Chưa chạy. 4 TC ([`03-TC-thu-muc-publish.md`](03-TC-thu-muc-publish.md)) + cascade SM-BIEUMAU.
  - **Cần có sẵn:** `[need: ≥3 TM CONG_KHAI candidate có ≥1 BM bên trong (✗ chờ T-FR09-002)]`

### CR-01 4 trường công khai

- 🟢 **T-FR09-007** CR-01 core (BM-CR-001..004) Switch toggle + auto timestamp + BR-PUBLIC-01..03 <a id="t-fr09-007"></a>
  - **Kết quả:** Chưa chạy. 4 TC gate cứng release ([`05-TC-bieu-mau-cong-khai-cr01.md`](05-TC-bieu-mau-cong-khai-cr01.md)).
  - **Cần có sẵn:** `[need: ≥3 BM state NHAP có ≥1 LV ref valid (✗ chờ T-FR09-002)]`

- 🟢 **T-FR09-008** CR-01 edge (BM-CR-005..012) — ảnh đại diện type/size, soft-delete reject, atomic unpublish, PDF 2-enum (G2), loai_hinh G11, mo_ta_cong_khai render <a id="t-fr09-008"></a>
  - **Kết quả:** Chưa chạy. 8 TC ([`05-TC-bieu-mau-cong-khai-cr01.md`](05-TC-bieu-mau-cong-khai-cr01.md)).
  - **Cần có sẵn:** `[need: BA confirm SPEC-CLARIFY-09-V3 (atomic unpublish) + V4 (loai_hinh enum vs free-text) (✗ chờ BA)]`

### Upload / Edge

- 🟢 **T-FR09-009** Upload edge (BM-008..010) — ngắt mạng, virus ClamAV, optimistic lock 2 user <a id="t-fr09-009"></a>
  - **Kết quả:** Chưa chạy. 3 TC ([`04-TC-bieu-mau-crud.md`](04-TC-bieu-mau-crud.md)).
  - **Cần có sẵn:** `[need: ≥1 BM NHAP ref valid (✗ chờ T-FR09-002)]`

- 🟢 **T-FR09-010** Bulk import (IMP-001..006) — 50 file / 500MB boundary + WRN-IMP-01 mix + audit log <a id="t-fr09-010"></a>
  - **Kết quả:** Chưa chạy. 6 TC ([`07-TC-bieu-mau-import.md`](07-TC-bieu-mau-import.md)).
  - **Cần có sẵn:** `[need: ≥1 TM NHAP target + fixture 51 file dummy (✗ chờ T-FR09-001 + fixture prep)]`

### Permission

- 🟢 **T-FR09-011** Permission 11 role × 6 action (PERM-001..006) + isolation cross-don_vi + CB_PD BR-FLOW-07 + QTHT override <a id="t-fr09-011"></a>
  - **Kết quả:** Chưa chạy. 6 TC ([`09-TC-permission.md`](09-TC-permission.md)).
  - **Cần có sẵn:** `[need: 11 role account active (`_03` permission test) + ≥2 đơn vị BN/ĐP có BM riêng (✗ chờ T-FR09-002 + users.csv)]`

### API outbound + Regression

- 🟢 **T-FR09-012** API outbound FR-VII-07 (API-001..005) — mTLS/JWT/rate limit/filter `cong_khai=1` + `is_deleted=0` (S2) <a id="t-fr09-012"></a>
  - **Kết quả:** Chưa chạy. 5 TC ([`08-TC-api-outbound.md`](08-TC-api-outbound.md)).
  - **Cần có sẵn:** `[need: ≥3 BM CONG_KHAI + mTLS cert sandbox + JWT machine cert (✗ chờ T-FR09-002 + infra)]`

- 🟢 **T-FR09-013** Regression CR-01 rename + enum migration THU_MUC + HĐ TV move FR-14 (REG-001..005) <a id="t-fr09-013"></a>
  - **Kết quả:** Chưa chạy. 5 TC ([`10-TC-edge-regression.md`](10-TC-edge-regression.md)).
  - **Cần có sẵn:** `[need: QA-API DB query access verify CHECK constraint + residual data (✗ chờ DBA assign)]`

---

## Cross-module dependency

| Upstream | Entity | Trạng thái cần | Task chờ |
|---|---|---|---|
| FR-10 (Danh mục) | DM `LINH_VUC_PL` | ≥6 record active | T-FR09-001, T-FR09-003 |
| Users / Auth | 11 role `_01` + `_03` | active, không lock | T-FR09-011 |
| Infra | mTLS cert + JWT machine cert | sandbox config | T-FR09-012 |
| BA sign-off | SPEC-CLARIFY-09-V3 (atomic unpublish) + V4 (loai_hinh enum) | confirm | T-FR09-008 |
| DBA | DB query access | grant | T-FR09-013 |

---

## Defer (sau v1.1 sign-off, cycle 2)

- **G1** REG-006 version control no-version proof (SRS v3.5 không có `BIEU_MAU_VERSION`).
- **G3** Virus scan MIME spoof / ZIP bomb / async detection — security backlog.
- **G4** `mo_ta_cong_khai` max length boundary — SPEC-CLARIFY-09-V5.
- **G6** Soft-delete THU_MUC chứa BM `is_deleted=1` — backlog.
- **G7** Cascade publish 100 BM performance.
- **G8** `so_luot_tai` counter race condition.
- **G9** Column TVV permission matrix vs users.csv reconcile.
- **G10** REG-002 enum migration SQL method.
- **G12** FR-10 LINH_VUC_PL orphan render.
- **S1/S3/S4/S5/S6/S7/S8/S9** — backlog v1.2.
