# TODO — FR-03 — Đào tạo & Tập huấn

> File module FR-03 (Nhóm III Quản lý Đào tạo) sinh từ [test-plan.md](test-plan.md) v1.1 revised 2026-05-12 13:00:00.
>
> **Tham chiếu shared:** [`../../tasks/state-snapshot.md`](../../tasks/state-snapshot.md) (TBD) · [test-plan.md](test-plan.md) · [review.md](review.md)
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream
>
> **Task ID convention:** `T-FR03-XXX` — XXX = order.
>
> **Upstream global deps (mọi seed task cần):** `[need: ≥3 DN HOAT_DONG (✗ chờ T-FR07-XXX); ≥3 TVV HOAT_DONG (✗ chờ T-FR04-XXX); DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001)]`.

---

## Tổng hợp module

| Phase | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ | ❌ | Task IDs |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| **Seed** | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR03-001..008 |
| **Lifecycle** | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR03-009..013 |
| **Functional** | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR03-014..018 |
| **Permission** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR03-019..020 |
| **Tổng** | **20** | **20** | **0** | **0** | **0** | **0** | **0** | **0** |  |

---

## Group A — Seed (8 task)

- 🟢 **T-FR03-001** Seed Kế hoạch ĐT năm (KE_HOACH_DAO_TAO) 6 variants cấp TW/BN/ĐP × state NHAP/DA_DUYET
  - **Cần có sẵn:** `[need: ≥3 đơn vị TW/BN/ĐP (✗ chờ T-FR10-001 don_vi seed)]`
  - **Output:** `seed-checklist-t-fr03-001-kh-nam.md` + verify GET `/api/v1/ke-hoach-dao-taos?nam=2026` ≥6 records.

- 🟢 **T-FR03-002** Seed CTDT 6 variants DU_THAO link KH năm DA_DUYET (Mô hình A 3 cấp guard)
  - **Cần có sẵn:** `[need: ≥3 KE_HOACH_DAO_TAO DA_DUYET (✗ chờ T-FR03-001 advance state); DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001)]`
  - **Output:** `seed-checklist-t-fr03-002-ctdt.md` + verify GET `/api/v1/chuong-trinh-dao-taos` cover 5 LV.

- 🟢 **T-FR03-003** Seed Khóa học 8 variants DU_THAO link CTDT DA_DUYET (cover 5 LV × 2 hình thức)
  - **Cần có sẵn:** `[need: ≥3 CTDT DA_DUYET (✗ chờ T-FR03-009 lifecycle CTDT); ≥3 GIANG_VIEN HOAT_DONG (✗ chờ T-FR03-005); ≥3 TVV HOAT_DONG (✗ chờ T-FR04-XXX)]`
  - **Output:** `seed-checklist-t-fr03-003-khoa-hoc.md` cover 5 LV × {TRUC_TIEP, TRUC_TUYEN}.

- 🟢 **T-FR03-004** Seed Lịch học 6 variants (FR-III-22) cover 2 hình thức + tuần ≥3 buổi
  - **Cần có sẵn:** `[need: ≥3 KHOA_HOC DA_DUYET/DA_CONG_KHAI (✗ chờ T-FR03-010 lifecycle KH)]`
  - **Output:** `seed-checklist-t-fr03-004-lich-hoc.md` + verify ngay_hoc trong khoảng KH bat_dau/ket_thuc.

- 🟢 **T-FR03-005** Seed Giảng viên (create) — 6 variants entity GV cover 6 LV + 3 trình độ (FR-III-11 SCR-III-05)
  - **Cần có sẵn:** `[need: DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001)]`
  - **Output:** `seed-checklist-t-fr03-005-giang-vien-create.md`. **Note:** GV mới tạo default state có thể là TAM_DUNG hoặc DANG_GIANG_DAY — verify SRS §3.4.3 GV entity.

- 🟢 **T-FR03-006** Advance state GV → DANG_GIANG_DAY (HOAT_DONG) ≥3 GV cover 6 LV (consumer: dropdown chọn GV khi tạo khóa)
  - **Cần có sẵn:** `[need: ≥6 GV record (✗ chờ T-FR03-005)]`
  - **Verify:** GET `/api/v1/giang-viens?trangThai=DANG_GIANG_DAY` ≥3, cover ≥3 LV downstream.
  - **Output:** `seed-checklist-t-fr03-006-gv-advance.md`.

- 🟢 **T-FR03-007** Seed Học viên (create) — qua FR-III-04 đăng ký DKDT NHẬP_TAY, verify auto-tạo TAI_KHOAN + HOC_VIEN.tai_khoan_id link
  - **Cần có sẵn:** `[need: ≥1 KHOA_HOC DA_CONG_KHAI (✗ chờ T-FR03-010); ≥3 DN HOAT_DONG (✗ chờ T-FR07-XXX)]`
  - **Output:** `seed-checklist-t-fr03-007-hv-create.md` + verify HOC_VIEN record có `tai_khoan_id` non-null per spec `_DELTA-MAP-FR03.md:42`.

- 🟢 **T-FR03-008** Advance state HV → DA_DUYET (CB NV duyệt đăng ký) ≥3 HV per khóa
  - **Cần có sẵn:** `[need: ≥3 DANG_KY_DAO_TAO CHO_DUYET (✗ chờ T-FR03-007)]`
  - **Verify:** GET `/api/v1/dang-ky-dao-taos?trangThai=DA_DUYET` ≥3.
  - **Output:** `seed-checklist-t-fr03-008-hv-advance.md`.

---

## Group B — Lifecycle (5 task)

- 🟢 **T-FR03-009** Workflow CTDT — SM-CTDT 7 trạng thái: DU_THAO → CHO_DUYET → DA_DUYET (+ refinement TU_CHOI → CHO_DUYET Cách 2) + auto DA_DUYET → DANG_THUC_HIEN → HOAN_THANH
  - **Cần có sẵn:** `[need: ≥3 CTDT DU_THAO (✗ chờ T-FR03-002); cb_nv_tw_01 + cb_pd_tw_01 login OK]`
  - **Output:** `workflow-test-report-t-fr03-009-ctdt.md` cover 7 transitions per SRS line 1880-1889.

- 🟢 **T-FR03-010** Workflow Khóa học — SM-KHOAHOC 9 trạng thái (per SRS body line 1806-1825). **SPEC-CLARIFY chờ BA:** DELTA-MAP nói 11 state — nếu confirm, add 2 transition TU_CHOI + TU_CHOI_KQ
  - **Cần có sẵn:** `[need: ≥3 KHOA_HOC DU_THAO (✗ chờ T-FR03-003)]`
  - **Output:** `workflow-test-report-t-fr03-010-khoa-hoc.md` cover full 9 state + transition CHO_DUYET → DU_THAO rollback.

- 🟢 **T-FR03-011** Workflow Kế hoạch năm — SM-KH-DAO-TAO 5 trạng thái (NHAP → CHO_DUYET → DA_DUYET → DA_CONG_KHAI + refinement Cách 2 TU_CHOI → CHO_DUYET)
  - **Cần có sẵn:** `[need: ≥3 KH năm NHAP (✗ chờ T-FR03-001); cb_pd_tw_01 login OK]`
  - **Output:** `workflow-test-report-t-fr03-011-kh-nam.md` cover 7 transitions per SRS line 1846-1856.

- 🟢 **T-FR03-012** **FR-III-21 Phê duyệt Khóa học** (CHO_DUYET → DA_DUYET) — happy + negative (BR-AUTH-05 cùng cấp). **SPEC-CLARIFY:** SRS line 1827 ghi "KHÔNG có FR riêng" → chờ BA confirm
  - **Cần có sẵn:** `[need: ≥3 KHOA_HOC CHO_DUYET (✗ chờ T-FR03-010 Bước 2); cb_pd_tw_01 + cb_pd_dp_01 login OK]`
  - **Output:** `workflow-test-report-t-fr03-012-fr-iii-21.md` (cover TC-KDT-22 + TC-KDT-23 test-plan).

- 🟢 **T-FR03-013** Chấm điểm + cấp kết quả khóa (FR-III-17/18) — BR-KQ-01 auto-classify + BR-KQ-02 truth table 4 case (Đủ/Thiếu CC/Thiếu điểm/Thiếu cả 2). FR-III-19 Hướng B: KHÔNG còn PDF chứng nhận
  - **Cần có sẵn:** `[need: ≥3 KHOA_HOC DA_KET_THUC (✗ chờ T-FR03-010 Bước 5); ≥3 HV DA_DUYET (✗ chờ T-FR03-008); điểm danh + điểm thi đã nhập]`
  - **Output:** `workflow-test-report-t-fr03-013-kq-classify.md` cover TC-HV-06/07 test-plan.

---

## Group C — Functional (5 task)

- 🟢 **T-FR03-014** Switch `cong_khai` BR-PUBLIC-01..03 — 4 entity (KH năm + CTDT + KH + Bài giảng) × toggle on/off + 5 trường công khai (`anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`)
  - **Cần có sẵn:** `[need: ≥1 record DA_DUYET mỗi entity (✗ chờ T-FR03-001/002/003 + BAI_GIANG seed)]`
  - **Output:** `functional-test-report-t-fr03-014-public-switch.md` cover TC-KH-10 + TC-KDT-16..18.

- 🟢 **T-FR03-015** FR-III-19 Công bố + Hủy công bố KQ — happy (3 path) + ERR-CB-KQ-01/04/05 + BR-INTG-05 retry 3 lần Cổng PLQG
  - **Cần có sẵn:** `[need: ≥1 KHOA_HOC HOAN_THANH có ≥1 KQ DA_DUYET (✗ chờ T-FR03-013)]`
  - **Output:** `functional-test-report-t-fr03-015-cong-bo-huy.md` cover TC-KDT-19/20/21 + TC-KDT-24.

- 🟢 **T-FR03-016** Junction `KHOA_HOC_GIANG_VIEN.vai_tro` override `GIANG_VIEN.loai` — cùng 1 GV TRO_GIANG khóa A + GIANG_VIEN khóa B → verify tab Lịch sử giảng dạy
  - **Cần có sẵn:** `[need: ≥1 GV link 2 khóa khác vai_tro (✗ chờ T-FR03-006 + T-FR03-003)]`
  - **Output:** `functional-test-report-t-fr03-016-junction-vai-tro.md` cover TC-GV-07 (SRS line 1714, 1784-1798).

- 🟢 **T-FR03-017** Cross-link FR-04 TVV `HOAT_DONG` → `KHOA_HOC.giang_vien_ids` — dropdown khi tạo khóa hiển thị cả GV nội bộ + TVV `HOAT_DONG` (verify enum rename `DANG_HOAT_DONG → HOAT_DONG`)
  - **Cần có sẵn:** `[need: ≥3 GV DANG_GIANG_DAY (✗ chờ T-FR03-006); ≥3 TVV HOAT_DONG (✗ chờ T-FR04-XXX)]`
  - **Output:** `functional-test-report-t-fr03-017-tvv-cross-link.md` cover TC-GV-08.

- 🟢 **T-FR03-018** Functional CRUD + search KH năm / CTDT / KH / Lịch học / Đề KT / GV / HV — 13 TC P0/P1 happy + negative ERR-* messages
  - **Cần có sẵn:** `[need: seed group A xong (✗ chờ T-FR03-001..008)]`
  - **Output:** `functional-test-report-t-fr03-018-crud-search.md` cover TC-KH-01..06 + TC-KDT-01..15 + TC-HV-01..10 + TC-GV-01..06.

---

## Group D — Permission (2 task)

- 🟢 **T-FR03-019** Permission Giảng viên (chuyên trang) — verify GV xem khóa được phân + GV xem self profile + GV KHÔNG xem GV khác
  - **Cần có sẵn:** `[need: ≥1 GV TK login OK + ≥1 KHOA_HOC link GV qua junction (✗ chờ T-FR03-006 + T-FR03-016)]`
  - **Output:** `permission-test-report-t-fr03-019-gv.md`.

- 🟢 **T-FR03-020** Permission Học viên (chuyên trang) — HV xem KQ self + KH đăng ký + KHÔNG xem KQ HV khác (BR-AUTH-08) + permission matrix full
  - **Cần có sẵn:** `[need: ≥1 HV TK login OK + ≥1 KET_QUA_DAO_TAO HOAN_THANH (✗ chờ T-FR03-007 + T-FR03-013)]`
  - **Output:** `permission-test-report-t-fr03-020-hv.md` cover TC-HV-08 + full matrix HV row.

---

## Note ngày handoff

> **2026-05-12 13:00:00** — Sinh todo.md từ test-plan.md v1.1 revised. 20 task pending: 8 seed + 5 lifecycle + 5 functional + 2 permission. Tất cả 🟢 sẵn sàng nhưng dep cross-module (T-FR04 TVV, T-FR07 DN, T-FR10 don_vi/LINH_VUC) còn ✗ — phải seed thượng nguồn trước. SPEC-CLARIFY blocker: (1) SM-KHOAHOC 9 vs 11 state, (2) FR-III-21 có phải FR độc lập, (3) Junction vai_tro Lịch sử giảng dạy derive đâu. BA sign-off trước Bước 4 viết file TC detail 01..04.
