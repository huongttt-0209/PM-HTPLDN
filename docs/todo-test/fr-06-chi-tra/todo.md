# TODO — FR-06 — Chi trả chi phí (XL)

> **Module size:** XL — 14 FR (V.II-01..14) · 4 entity owned (HSCT + DANH_GIA + THAM_DINH v3.5 + PHE_DUYET v3.5) · 10-state SM · 14 transition · 5 BR-CALC · 3 quy mô × trần năm boundary
>
> **Test plan:** [test-plan.md](./test-plan.md) (Revised 2026-05-12 13:30:00 — 63 TC, 11 file con)
> **Review:** [review.md](./review.md) (REVISE → APPROVE sau revise apply ≥80%)
>
> **Cross-module upstream BẮT BUỘC sẵn sàng TRƯỚC khi chạy task functional:**
>
> `[need: ≥3 VV state HOAN_THANH (✗ chờ T-FR05-XXX); ≥3 HĐ TVPL đã ký (✗ chờ T-FR14-XXX); ≥3 DN HOAT_DONG cover 3 quy mô SIEU_NHO/NHO/VUA (✗ chờ T-FR07-XXX); DM TIEU_CHI_DG_CP 3 quy mô với tran_ho_tro_nam (✗ chờ T-FR10-XXX DM); ≥1 NGAY_LE FR-VIII-29 seed (✗ chờ T-FR10-XXX); ≥1 TVV HOAT_DONG (✗ chờ T-FR04-XXX)]`
>
> **Icon meaning:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream

---

## Tasks

### Nhóm A — Chặn nhập tay UI (đặc thù module, system-overview §4.12:717)

- 🟢 **T-FR06-001** Verify 7 role × SCR-V.II-01 KHÔNG render nút [Thêm mới] / [Tạo HS chi trả]
  - **TC:** TC-LIST-04 — Test method UI (MCP `isolatedContext` per role × 7)
  - **Role list:** QTHT, CB_NV_TW, CB_NV_BN, CB_NV_DP, CB_PD_TW, CB_PD_BN, CB_PD_DP
  - **Cần có sẵn:** [need: 7 account login OK (✗ verify users.csv); SCR-V.II-01 render OK (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-002** DOM grep absence button [Auto từ chối quá hạn] / [Auto từ chối lần 4]
  - **TC:** TC-LIST-05 — verify Δ Thay đổi 5 OUT (`_DELTA-MAP-FR06.md:56`)
  - **Cần có sẵn:** [need: SCR-V.II-01 render với HS YEU_CAU_BO_SUNG (✗)]
  - **Kết quả:** TBD

### Nhóm B — LGSP Inbound (DVC HSCT)

- 🟢 **T-FR06-003** LGSP inbound JWT hợp lệ + Mẫu 01 NĐ55 18 trường → INSERT HSCT CHO_TIEP_NHAN
  - **TC:** TC-API-01, TC-API-03 (auto-gen mã CT-YYYYMMDD-SEQ)
  - **Cần có sẵn:** [need: LGSP mock server up (✗ chờ Infra); JWT keypair LGSP sandbox (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-004** LGSP inbound negative — JWT/payload invalid + idempotent key
  - **TC:** TC-API-02 (JWT invalid 401), TC-API-04 (thiếu trường 400), TC-API-06 (dup ma_ho_so_dvc 409)
  - **Kết quả:** TBD

- 🟢 **T-FR06-005** Cross-ref FR-05 — payload reference VV state ≠ HOAN_THANH → reject 400
  - **TC:** TC-API-07 (G3 fix)
  - **Cần có sẵn:** [need: ≥1 VV state DANG_XU_LY (✗ chờ T-FR05-XXX); ≥1 VV state HOAN_THANH baseline (✗ chờ T-FR05-XXX)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-006** Cross-ref FR-14 — payload `so_hop_dong_tvpl` không tồn tại trong FR-14 → reject/warning
  - **TC:** TC-API-08 (G4 fix)
  - **Cần có sẵn:** [need: ≥3 HĐ TVPL đã ký FR-14 (✗ chờ T-FR14-XXX); 1 mã HĐ giả KHÔNG tồn tại (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-007** LGSP outbound retry 3 lần × 30s timeout
  - **TC:** TC-API-05
  - **Cần có sẵn:** [need: LGSP outbound mock có thể inject timeout (✗ chờ Infra)]
  - **Kết quả:** TBD

### Nhóm C — State lifecycle 10 state + 14 transition

- 🟢 **T-FR06-008** Tiếp nhận + Rút HS (transition 2, 3)
  - **TC:** TC-TN-01..05 (5 TC)
  - **Cần có sẵn:** [need: ≥3 HSCT state CHO_TIEP_NHAN (✗ tự seed qua T-FR06-003 LGSP inbound)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-009** Kiểm tra HS Mẫu 01 (transition 4, 5, 6)
  - **TC:** TC-KT-01, TC-KT-02
  - **Cần có sẵn:** [need: ≥3 HSCT state DANG_KIEM_TRA (✗ tự seed)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-010** Đánh giá DANG_THAM_DINH transition + thẩm định DAT/KHONG_DAT (transition 8, 10)
  - **TC:** TC-TD-01..04 (UNIQUE constraint THAM_DINH 1:1)
  - **Cần có sẵn:** [need: ≥3 HSCT state DANG_DANH_GIA với DM TIEU_CHI_DG_CP đủ 3 quy mô (✗ chờ T-FR10-XXX DM); ≥3 DN cover 3 quy mô (✗ chờ T-FR07-XXX)]
  - **Kết quả:** TBD

### Nhóm D — Thẩm định + Trình PD + Phê duyệt (FR-V.II-09/11/12, Δ v3.5)

- 🟢 **T-FR06-011** BR-FLOW-05 — Thẩm định DAT → state vẫn DANG_THAM_DINH (KHÔNG auto chuyển), [Trình PD] manual mới sang CHO_PHE_DUYET
  - **TC:** TC-FLOW-02, TC-TD-03 (Trình PD khi ket_qua ≠ DAT → ERR-CT-TRINH-01)
  - **Kết quả:** TBD

- 🟢 **T-FR06-012** CB PD [Phê duyệt] / [Từ chối — trả về DANG_THAM_DINH] (Δ v3.5)
  - **TC:** TC-PD-01..05 (5 TC) + TC-PD-02 verify `thoi_gian_tu_choi IS NULL` (G10 fix)
  - **Cần có sẵn:** [need: ≥3 HSCT state CHO_PHE_DUYET với CB PD cùng đơn vị (✗); cb_pd_tw_01 + cb_pd_bn_01 + cb_pd_dp_01 login OK (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-013** PHE_DUYET_CHI_TRA N:1 lifecycle — CB PD trả về nhiều lần + CB NV trình lại
  - **TC:** TC-FLOW-01 (2 lần TU_CHOI + 1 DUYET), TC-PD-02b (sau trả về [Trình PD] lại) — S5 add
  - **Kết quả:** TBD

- 🟢 **T-FR06-014** CB PD reject lý do < 10 ký tự + thiếu so_tien_duyet + so_tien_duyet > so_tien_de_nghi
  - **TC:** TC-PD-03, TC-PD-04, **TC-PD-05** (G13 fix — boundary EC-02)
  - **Kết quả:** TBD

### Nhóm E — DN bổ sung 3 lần loop + BA escalate lần 4 (FR-V.II-14, Δ v3.5)

- 🟢 **T-FR06-015** Happy P0 — Loop 3 lần bổ sung — bo_sung_count 1→2→3 + UI highlight đỏ ≥2
  - **TC:** TC-BS-01 (file PDF ≤10MB ≤5 ngày), **TC-BS-05a** (G2 split happy 3 loop)
  - **Cần có sẵn:** [need: ≥1 HSCT state YEU_CAU_BO_SUNG seed lần 1 (✗); DN account 9999999990 login OK (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-016** Negative bổ sung — file 11MB / .exe / > 5 ngày LV
  - **TC:** TC-BS-02 (11MB), TC-BS-03 (.exe), TC-BS-04 (quá 5 ngày)
  - **Cần có sẵn:** [need: ≥1 HSCT state YEU_CAU_BO_SUNG với ngay_yeu_cau_bo_sung lùi 6+ ngày LV (✗ tự seed DB)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-017** Edge P1 defer — Lần 4 bổ sung (bo_sung_count=4 không trong CHECK 0..3) hành vi chờ BA Q1 → mark 🤷 nhóm C BA
  - **TC:** **TC-BS-05b** (G2 split)
  - **Note:** không kết luận, defer BA confirm trước khi log bug. Per CLAUDE.md `deep_review_before_ba_defer` — retry method (curl backend trực tiếp) trước mark 🤷.
  - **Kết quả:** TBD (defer)

### Nhóm F — BR-CALC 3 quy mô × trần năm boundary (FR-V.II-05)

- 🟢 **T-FR06-018** Happy 3 quy mô — SIEU_NHO 100%/3M, NHO 30%/5M, VUA 10%/10M
  - **TC:** TC-CALC-01, TC-CALC-02, TC-CALC-03
  - **Cần có sẵn:** [need: ≥1 DN mỗi quy mô (✗ chờ T-FR07-XXX); DM TIEU_CHI_DG_CP 3 quy mô (✗ chờ T-FR10-XXX)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-019** Edge BR-CALC-02 — boundary trần năm + EC-01 (phí=0) + EC-05 (hết trần)
  - **TC:** TC-CALC-04 (hết trần), TC-CALC-05 (phí 0), TC-CALC-06 (vượt trần năm), TC-CALC-07 (boundary clip trần), TC-CALC-08 (% nhỏ hơn)
  - **Kết quả:** TBD

- 🟢 **T-FR06-020** Edge BR-CALC-04 snapshot — DN đổi quy mô qua FR-07 update endpoint không ảnh hưởng HS đã tính
  - **TC:** **TC-CALC-09** (G5 rework — step 1-4 rõ)
  - **Cần có sẵn:** [need: ≥1 DN SIEU_NHO HOAT_DONG (✗ chờ T-FR07-XXX); FR-07 endpoint update DN.quy_mo OK (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-021** Edge G6 add — boundary EXACT trần + reset 1/1 năm mới
  - **TC:** **TC-CALC-11** (da_chi exact = trần → 0 + cảnh báo), **TC-CALC-12** (HS 2025 → 2026 reset)
  - **Cần có sẵn:** [need: clock mock hoặc DB seed `ngay_nop` năm 2025 vs 2026 (✗)]
  - **Kết quả:** TBD

### Nhóm G — Permission BR-AUTH-05/08 + Δ v3.5 2 cấp (BR-AUTH-02)

- 🟢 **T-FR06-022** Cross-unit BR-AUTH-08 — CB NV BN BKH chỉ thấy HS BKH (không BTC)
  - **TC:** TC-PERM-01, TC-PERM-02
  - **Cần có sẵn:** [need: ≥1 HSCT thuộc BKH + ≥1 thuộc BTC (✗); cb_nv_bn_01 BKH + cb_nv_bn_02 BTC login OK (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-023** Cross-cấp BR-AUTH-08 — CB NV DP AG chỉ thấy HS STP-AG
  - **TC:** TC-PERM-03
  - **Cần có sẵn:** [need: ≥1 HSCT thuộc STP-AG; cb_nv_dp_01 AG login OK (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-024** Cross-unit BR-AUTH-05 — CB PD BN BKH KHÔNG được phê duyệt HS BTC + CB PD DP duyệt HS TW
  - **TC:** TC-PERM-04, TC-PERM-05
  - **Cần có sẵn:** [need: ≥1 HSCT BTC state CHO_PHE_DUYET; cb_pd_bn_01 BKH + cb_pd_dp_01 AG login OK (✗)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-025** Permission negative — DN không vào CMS / TVV scope mình
  - **TC:** TC-PERM-06 (DN 403), **TC-PERM-07a** (TVV không match → 403), **TC-PERM-07b** (TVV match → mark 🤷 BA — G7 split)
  - **Kết quả:** TBD

- 🟢 **T-FR06-026** Δ v3.5 BR-AUTH-02 — account cấp cũ (HUYEN/XA) thử Read HSCT → 403 hoặc map về DP
  - **TC:** **TC-PERM-08** (G11 add)
  - **Cần có sẵn:** [need: verify users.csv có account cấp HUYEN/XA legacy không (✗); BA confirm hành vi (✗)]
  - **Kết quả:** TBD

### Nhóm H — Migration v3 → v3.5 (enum + entity mới)

- 🟢 **T-FR06-027** Enum cũ BỎ — verify mọi state response API KHÔNG còn `MOI`/`DA_TIEP_NHAN`/`CHO_THAM_DINH`/`DA_THAM_DINH`/`TU_CHOI_THAM_DINH`/`TU_CHOI_THANH_TOAN`
  - **TC:** TC-SM-01 (verify enum trong DB schema CHECK constraint + response API mới 10 enum)
  - **Cần có sẵn:** [need: DB migration v3.5 đã chạy (✗ chờ Dev BE)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-028** Entity mới THAM_DINH_HO_SO 1:1 + PHE_DUYET_CHI_TRA N:1 (BR-SCHEMA-04/05)
  - **TC:** TC-TD-04 (INSERT THAM_DINH lần 2 cùng HS → UNIQUE violation), TC-FLOW-01 (PHE_DUYET N:1)
  - **Kết quả:** TBD

### Nhóm I — Cross-cutting CR-01/02 + Audit + Edge

- 🟢 **T-FR06-029** Audit log full coverage 14 transition (split G14)
  - **TC:** **TC-AUDIT-01a** (transition 1-7), **TC-AUDIT-01b** (transition 8-14)
  - **Kết quả:** TBD

- 🟢 **T-FR06-030** SLA tính qua ngày lễ + Optimistic lock + Pagination + Hard-delete + Public endpoint
  - **TC:** TC-EDGE-01 (SLA qua Tết, cần FR-VIII-29 NGAY_LE), **TC-EDGE-02** (S9 detail version conflict), TC-LIST-02a/b (G12 split), TC-CR-01 (defer BA G8), TC-CR-02 (401 public)
  - **Cần có sẵn:** [need: ≥1 NGAY_LE FR-VIII-29 seed (✗ chờ T-FR10-XXX); admin SQL access cho TC-CR-01 hard-delete (✗ chờ Infra/DBA)]
  - **Kết quả:** TBD

- 🟢 **T-FR06-031** Notification outbound success (G9 add) + outbound LGSP retry log
  - **TC:** **TC-NOTIF-02** (G9 — DVC outbound / in-app TVV / email), TC-API-05 (retry log)
  - **Cần có sẵn:** [need: in-app TVV login huongcg OK (✗); email mock MailHog up (✓ standard)]
  - **Kết quả:** TBD

### Nhóm J — Cross-module smoke regression (S10 verdict gate)

- 🟢 **T-FR06-032** Smoke 5 phút FR-05 (VV HOAN_THANH render) + FR-07 (DN quy_mo update) + FR-14 (HĐ TVPL list) không break sau khi FR-06 PASS
  - **TC:** smoke nhóm C IMPACT — mỗi module render OK + KPI count match baseline
  - **Cần có sẵn:** [need: FR-06 P0 PASS 100% trước (✗)]
  - **Kết quả:** TBD

### Nhóm K — Edge case hunter review (REQUIRED cho XL module — S11)

- 🟢 **T-FR06-033** Chạy 11-REVIEW-edge-case-hunter.md — combinatorial edge: quy_mo × state × bo_sung_count × cấp × ngày LV
  - **Note:** Per CLAUDE.md Rule 4 — XL module 14 FR + 5 BR-CALC + cross-cutting → edge-case-hunter pass đáng giá để catch combinatorial gap không cover trong 32 task trên.
  - **Kết quả:** TBD

---

*Generated 2026-05-12 13:30:00 sau revise test-plan v1.1. Total 33 task — XL module. Upstream cross-module dependencies: FR-04 (TVV), FR-05 (VV HOAN_THANH), FR-07 (DN 3 quy mô), FR-10 (DM TIEU_CHI_DG_CP + NGAY_LE FR-VIII-29), FR-14 (HĐ TVPL). 1 task defer 🤷 BA (T-FR06-017 lần 4 bổ sung). 1 task chờ Infra/DBA (T-FR06-030 hard-delete).*
