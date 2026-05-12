# TODO — FR-10 QTHT — Quản trị hệ thống

> **Phiên bản:** 1.0 — generated 2026-05-12 12:40:00 from [test-plan.md](test-plan.md) v1.1 (Revised) sau review feedback.
>
> **Module class:** L (27 FR · 10 SCR · 4 BR mới · SM-TAIKHOAN 8 transition / 9 trigger · 197 TC dự kiến).
> **Tầng phụ thuộc:** FR-10 là **Tầng 1 nền tảng — KHÔNG có upstream module**. Mọi module nghiệp vụ khác depend FR-10 seed (DM/Đơn vị/Vai trò/TK).
> **Task ID:** `T-FR10-XXX` (plan-stage; sẽ map sang round actual `R{N}.{phase}.{seq}` khi chạy).
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream · ❌ FAIL.
>
> **Tham chiếu:** [test-plan.md](test-plan.md) · [review.md](review.md) · `tasks/todo-qtht.md` (round actual) · [permission-matrix.md](../../../output/permission-matrix.md) · [users.csv](../../../input/users.csv)

---

## Tổng hợp

| Cụm | Tổng task | TC dự kiến | Status |
|---|:-:|:-:|---|
| Seed Tầng 1 (DM + Đơn vị + Vai trò + TK + SLA + Ngày lễ) | 5 | (seed gates) | 🟢 5/5 |
| Workflow + Functional 14 DM CRUD | 3 | 36 | 🟢 3/3 |
| Functional auth + account + permission | 5 | 78 | 🟢 5/5 |
| Edge / Permission / Audit / VNeID | 4 | 53 | 🟢 4/4 |
| Pre-execution unblock (BA escalation) | 1 | (gating) | 🟢 1/1 |
| **TỔNG** | **18** | **≈197** | **🟢 18/18 sẵn sàng** |

---

## Tasks

### Cụm A — Pre-execution unblock

- 🟢 **T-FR10-001** BA escalation — chốt 9 GAP register Phụ lục C.1 trước khi viết TC detail
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: BA confirm GAP-VIII-04 (password regex) + GAP-EXPORT-10K-ERR + GAP-EXCEL-IMPORT-SCHEMA-ERR + GAP-AUDIT-ROLE + GAP-VNEID-FLAG (✗ chưa escalate)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/ba-escalation-r{N}.md`

### Cụm B — Seed Tầng 1 (data foundation)

- 🟢 **T-FR10-002** Seed 14 tab DM (Lĩnh vực PL / Loại HT / CT HT / TT VV / Loại DN / Hồ sơ HT/TT / Tiêu chí HQ/CP / Loại TK / LH TN / Kênh TN / Tỉnh-Thành / Cơ quan ĐV)
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** FR-10 là Tầng 1 nền tảng, không có upstream module.
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/seed-checklist-dm-14tab.md`

- 🟢 **T-FR10-003** Seed DON_VI cây 2 tầng (TW + 3 BN + 3 DP ≥) — verify BR-AUTH-02 BN/DP ngang cấp
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 record DM TINH_THANH (✗ chưa seed) — FK FR-VIII-30]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/seed-checklist-don-vi.md`

- 🟢 **T-FR10-004** Seed VAI_TRO + QUYEN_HAN + TAI_KHOAN ≥1 per role (12 role × ≥1) — verify Permission Matrix §2.3.1
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 DON_VI mỗi cấp TW/BN/DP (✗ chưa seed) + ≥1 DM_LOAI_TK (✗ chưa seed)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/seed-checklist-vai-tro-tk.md`

- 🟢 **T-FR10-005** Seed CAU_HINH_SLA 4 loại yêu cầu (Hỏi đáp / Vụ việc / HSHT / HSTT) — verify BR-SLA-01/02/04
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 record DM LOAI_HINH_HT (✗ chưa seed) — FK ngày lễ trừ NGAY_LE]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/seed-checklist-sla.md`

- 🟢 **T-FR10-006** Seed NGAY_LE 2026 (≥5 ngày: Tết / 30-4 / 1-5 / 2-9 / 10-3 ÂL)
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** FR-10 nền tảng — không upstream.
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/seed-checklist-ngay-le.md`

### Cụm C — Workflow + Functional 14 DM CRUD

- 🟢 **T-FR10-007** Functional 14 DM CRUD (FR-VIII-01..09/11/12/13/18/19) — TPL-DM-CRUD + happy/negative + ERR-DM-01..05 + BR-DATA-01/06 + BR-EC-01/13 + BR-UX-01
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥6 LV PL + ≥4 Loại DN + ≥1 record/14 tab DM (✗ chưa seed — T-FR10-002 gate)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-14dm.md`

- 🟢 **T-FR10-008** Functional Cơ quan đơn vị tree 2 tầng (FR-VIII-05) — BR-AUTH-02/04 + ERR-DV-01..05 (vòng lặp + cascade delete)
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 TW + ≥1 BN + ≥1 DP (✗ chưa seed — T-FR10-003 gate)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-coquandonvi.md`

- 🟢 **T-FR10-009** Functional Tỉnh/Thành 63 GSO read-only (FR-VIII-30) — verify count = 63, chỉ đổi `trang_thai`
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: seed deploy 63 GSO record (✗ chưa verify)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-tinh-thanh.md`

### Cụm D — Functional auth + account + permission

- 🟢 **T-FR10-010** Functional Vai trò CRUD (FR-VIII-14) — ERR-VT-01/02 + BR-EC-01
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: account `qtht_01` HOAT_DONG (✗ chưa verify lifecycle)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-vai-tro.md`

- 🟢 **T-FR10-011** Functional Tài khoản NSD + SM-TAIKHOAN 8 transition / 9 trigger (FR-VIII-15) — ERR-TK-01..06 + BR-AUTH-USERNAME/EMAIL-01
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 VAI_TRO + ≥1 DON_VI + ≥1 DM_LOAI_TK (✗ chưa seed — T-FR10-004 gate)]
  - **Bug:** placeholder — sẽ link file `bug-report-tai-khoan-rN.md` khi chạy round.
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-tai-khoan.md`

- 🟢 **T-FR10-012** Functional Phân quyền dữ liệu (FR-VIII-16) — BR-AUTH-03/04/08 + ERR-PQ-01..04 + cross-unit query 0 rows
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥3 TK CB_NV_BN + ≥3 TK CB_NV_DP khác don_vi_id (✗ chưa seed — T-FR10-004 gate)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-phanquyen-data.md`

- 🟢 **T-FR10-013** Functional Phân quyền chức năng (FR-VIII-17) — checkbox cây menu cha-con + [Reset mặc định]
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 VAI_TRO + ≥1 QUYEN_HAN seed (✗ chưa seed — T-FR10-004 gate)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-phanquyen-cn.md`

- 🟢 **T-FR10-014** Functional Đăng nhập / Đăng xuất Tier 1 TOTP (FR-VIII-20/21) — BR-AUTH-06/07 + 5-fail lock + 30' idle + ERR-DN-01..08
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 TK HOAT_DONG (✗ chưa seed — T-FR10-004 gate)]
  - **Bug:** placeholder.
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-dangnhap.md`

### Cụm E — Edge / Permission / Audit / VNeID

- 🟢 **T-FR10-015** Functional DN self-reg MST (FR-VIII-22) — 18 trường form + Phương án B email + cam kết + ERR-REG-01..06 + idempotency
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 DM Tỉnh/Thành + ≥1 DM Loại DN (✗ chưa seed — T-FR10-002 gate) + GAP-VIII-04 password regex BA chốt]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-self-reg-dn.md`

- 🟢 **T-FR10-016** Functional VNeID 3 luồng + BR-AUTH-09 (FR-VIII-23/24/25) — ERR-VN-01..04 + CB nội bộ KHÔNG VNeID
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: Tier 2 VNeID feature flag ON (✗ chưa enable — GAP-VNEID-FLAG)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-vneid.md`

- 🟢 **T-FR10-017** Functional Quên MK + Kích hoạt TK lần đầu (FR-VIII-26) — ERR-PWD-01..06 + chống enumerate + idempotency token reset
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥1 TK CHO_KICH_HOAT (✗ chưa seed — T-FR10-004 gate)]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-quen-mk.md`

- 🟢 **T-FR10-018** Functional Audit log + Ngày lễ CRUD/Import (FR-VIII-28/29) — cap 90 ngày + export 10K + ERR-LOG-01/02 + ERR-NL-01..03 + Excel import schema
  - **Kết quả:** TBD — chưa chạy round.
  - **Cần có sẵn:** [need: ≥100 audit entry (✗ chưa seed) + GAP-EXPORT-10K-ERR + GAP-EXCEL-IMPORT-SCHEMA-ERR BA chốt]
  - **Output:** `docs/todo-test/fr-10-qtht/results/<round>/functional-test-report-audit-ngayle.md`

---

## Module không có upstream

FR-10 QTHT là **Tầng 1 nền tảng** trong hệ thống HTPLDN. Mọi seed entity (DM / Đơn vị / Vai trò / TK / SLA / Ngày lễ) là input của các module nghiệp vụ downstream (FR-02 Hỏi đáp, FR-04 Tư vấn cơ bản, FR-05 Tư vấn chuyên sâu, FR-06 Hồ sơ HT, FR-07 Hồ sơ TT, ...).

**Downstream depend FR-10 ra sao:**
- DM (14 tab) → mọi module dropdown
- DON_VI → mọi module có `don_vi_id` (BR-AUTH-08)
- VAI_TRO + QUYEN_HAN → permission check mọi action
- TAI_KHOAN → tạo TVV/CG/NHT auto-tạo qua FR-04
- CAU_HINH_SLA → FR-02/04/05/06/07 deadline calc
- NGAY_LE → SLA deadline trừ ngày lễ
- AUDIT_LOG → mọi module CUD ghi vào

---

## Note phiên bản

> `2026-05-12 12:40:00` — todo.md sinh từ test-plan.md v1.1 (Revised) sau review feedback. 18 task plan-stage, mọi task 🟢 sẵn sàng. Khi flip ⏳/🔵/✅, ghi lại round actual + report link cụ thể.
