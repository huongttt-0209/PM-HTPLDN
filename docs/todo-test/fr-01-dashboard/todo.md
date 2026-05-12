# TODO — fr-01-dashboard — Dashboard 9 KPI + 2 chart

> **Module:** FR-01 Dashboard (SCR-I-01) — Tầng 5 (tổng hợp đầu ra), nhóm C IMPACT only.
> **Test plan:** [test-plan.md](test-plan.md) — 66 TC × 15 file × 8 cross-module integration.
> **Round:** R1-FR01 (test-plan sign-off pending BA Q1/Q2/Q3/Q4).
> **Phụ thuộc upstream:** FR-02 (HOI_DAP), FR-03 (KHOA_HOC + KET_QUA_DAO_TAO), FR-04 (TU_VAN_VIEN), FR-05 (VU_VIEC + audit log), FR-08 (KET_QUA_DANH_GIA — đã rename), FR-10 (CAU_HINH_SLA + DON_VI tree).

## Icon meaning

- 🟢 Sẵn sàng chạy (dep upstream ✓)
- ⏳ Chờ upstream (dep ✗ — xem `**Cần có sẵn:**`)
- 🚫 Block không-task (chờ BA / infra / dev)
- ✅ Đạt
- ⚠️ Sai spec
- ❌ Lỗi
- 🤷 Không xác định (cần retry method)

---

## Tracker — Round 1 (FR-01 Dashboard)

- ⏳ **T-FR01-001** Smoke login 11 role + load SCR-I-01
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: 11 account trong users.csv login OK (✓ schema 11 cột verified 2026-04-24)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-002** KPI-01 Hỏi đáp mới — TC-01.1/01.2/01.3/01.4 (FR-I-01)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥5 HOI_DAP state=MOI ngay_tao trong kỳ ĐP-AG (✗ — FR-02 task seed HD-001 chưa PASS)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-003** KPI-02/03/04 VV core — TC-02.x/03.x/04.x + 5-state-sống G1
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 VU_VIEC mỗi 5 state sống + ≥3 HOAN_THANH (✗ — FR-05 R-VV-001/002/003 chưa PASS)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-004** KPI-05/06 Khóa học — TC-05.1/06.1 (S2 cross-module mới)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥4 KHOA_HOC DANG_DIEN_RA + ≥3 DA_KET_THUC ĐP-AG (✗ — FR-03 R-DT-001/002 chưa PASS)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-005** KPI-07 CG/TVV snapshot — TC-07.1/07.2/07.3
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥4 TU_VAN_VIEN DANG_HOAT_DONG + ≥2 TAM_DUNG ĐP-AG (✗ — FR-04 R-TVV-001 chưa PASS)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-006** UC8 2 biểu đồ cột — TC-08.1/08.2/08.3 + BR-SLA-05 v3.5
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: 5 VV đúng hạn + 2 trễ + 3 DANG_XU_LY quá hạn + ≥5 KET_QUA_DANH_GIA diem_tong (✗ — FR-05 + FR-08 + CAU_HINH_SLA chưa sẵn)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-007** UC8 N<10 mẫu nhỏ — TC-08.4/08.5 (G6)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: pool nhỏ <10 cho UC8 trái + phải (subset T-FR01-006 data)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-008** UC9 donut đào tạo — TC-09.1/09.2/09.3 + N<10
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥12 KET_QUA_DAO_TAO ĐP-AG xep_loai + diem_kiem_tra (✗ — FR-03 R-DT-003 chưa PASS)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-009** KPI-S-01/S-02 supplementary + BR-CALC-03
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: 10 VV HOAN_THANH + 3 từng qua YEU_CAU_BO_SUNG (audit log) + CAU_HINH_SLA ngày LV (✗ — FR-05 history + FR-10 SLA)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-010** Auto-refresh 60s + per-widget + Page Visibility — TC-12.1..12.5 (G5)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: dashboard load OK 9 KPI + 3 chart + MCP evaluate_script throttle mock (✓ kỹ thuật khả thi)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- 🚫 **T-FR01-011** Banner-30 mock 6/12 widget × 3 chu kỳ — TC-12.6 (G8)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: infra mock timeout 30s × 3 chu kỳ ~3 phút setup (✗ — chờ infra confirm cách throttle, nhóm D)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-012** Filter Năm/Tháng/L1/L2 + URL sync — TC-13.1..13.6
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: DON_VI tree TW + ≥1 BN + ≥1 ĐP (✓ FR-10 đã có sẵn) + dashboard load OK]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- 🚫 **T-FR01-013** Filter DB rỗng Năm dropdown — TC-13.7 (G2)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: env clone rỗng + BA confirm Q1 default Năm (✗ — chờ BA, nhóm C)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-014** Drill-down 7 KPI giữ filter + legacy URL — TC-14.1..14.5 (G7)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: tất cả KPI render data (subset T-FR01-002..005)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-015** Permission 11 role + scope + chip + BN/ĐP cross-block — TC-15.1..15.10 (G10)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: 11 account login + scope data per role (subset T-FR01-001) + BA confirm Q4 chip QTHT (⚠️ nhóm C)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

- ⏳ **T-FR01-016** Trend chéo năm Y-1 tháng 12 — TC-01.3/01.4/03.4 (G9)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: audit log lịch sử state VU_VIEC Y-1 tháng 12 (✗ — FR-05 backdate seed chưa có, BE confirm cho phép)]
  - **Output:** docs/todo-test/fr-01-dashboard/results/r1/

---

## Cross-module dep summary

- **FR-02** (HOI_DAP MOI) → T-FR01-002.
- **FR-03** (KHOA_HOC DANG_DIEN_RA + DA_KET_THUC + KET_QUA_DAO_TAO) → T-FR01-004 + T-FR01-008.
- **FR-04** (TU_VAN_VIEN DANG_HOAT_DONG) → T-FR01-005.
- **FR-05** (VU_VIEC 5-state sống + HOAN_THANH + audit log lịch sử + Y-1 historical) → T-FR01-003 + T-FR01-006 + T-FR01-009 + T-FR01-016.
- **FR-08** (KET_QUA_DANH_GIA — module rename "Theo dõi Đánh giá HQ HTPL") → T-FR01-006.
- **FR-10** (CAU_HINH_SLA + DON_VI tree) → T-FR01-006 + T-FR01-009 + T-FR01-012.
- **BA Q1/Q3/Q4** → T-FR01-013 + T-FR01-003 (Δ3 v3 baseline) + T-FR01-015.
- **Infra** → T-FR01-011 (banner-30 throttle setup).

## Note 2026-05-12 15:10:00

Test plan v1.1 đã revise apply 10 gap + 8 suggestion từ review. Tất cả task ⏳ chờ upstream module FR-02/03/04/05/08/10. 2 task 🚫 (T-FR01-011 infra mock, T-FR01-013 BA confirm Q1). T-FR01-001 chỉ chờ env login OK (gần như 🟢) — ưu tiên chạy đầu để smoke 11 role trước khi block seed.
