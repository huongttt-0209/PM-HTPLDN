# TODO — FR-02 — Hỏi đáp

> Generated 2026-05-12 13:00:00 từ test-plan.md v1.1 (109 TC × 14 file) + review.md (3 Critical fix applied).
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream · ❌ FAIL
>
> **Tham chiếu shared:** [test-plan.md](test-plan.md) · [review.md](review.md) · [tasks/state-snapshot.md](../../../tasks/state-snapshot.md)
>
> **Source mode:** LOCAL — cite prefix `srs-update-2026-5-5/...` (v3.5) + `srs-v3/...` (baseline). Mọi BR/FR cite có file + line.

---

## Tổng hợp

| Phase | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ | ❌ |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Seed** (HD entry + MPH Hybrid + TVN) | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| **State lifecycle** (SM 10 trạng thái + BR-FLOW-01 auto) | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Phân công auto-filter 4 tiêu chí** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **SLA cảnh báo** (4 mức + cron + ngày lễ) | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Công khai + Hủy CK** (BR-FLOW-05 CR-01) | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Auto-tạo FR-13 Kho QA** (`nguon=TU_DONG`) | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Mẫu phản hồi Hybrid 2 tầng** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Permission cross-cap** (11×8 matrix) | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **BA escalate** (FR-II-NEW-01 + SLA 2/4 mức + Kho QA) | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Tổng** | **19** | **19** | 0 | 0 | 0 | 0 | 0 | 0 |

---

## Tasks

### Group 1 — Seed (3 task)

- 🟢 **T-FR02-001** Seed 6 HOI_DAP entry state MOI cover 6 lĩnh vực × 4 kênh tiếp nhận
  - **Kết quả:** Cần seed ≥6 record state MOI qua UI Drawer SCR-II-01.
  - **Cần có sẵn:** [need: ≥6 LV trong DM LINH_VUC_PL state ACTIVE (✗ chờ T-FR10-001); DON_VI tree 2 tầng TW/BN/DP (✓ R1 seed); CB_NV `cb_nv_tw_01` login OK (✓)]
  - **Spec:** `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:99,1519` (CR-06 routing) + §SCR-II-01 Drawer (test-plan §2.4)
  - **Output:** `output/qa-reports/round{N}/seed/hoi-dap/seed-checklist-fr02-001-hd-moi.md`

- 🟢 **T-FR02-002** Seed Mẫu phản hồi Hybrid 2 tầng (TW_QUOC_GIA + BN_RIENG + DP_RIENG)
  - **Kết quả:** Cần ≥3 MAU_PHAN_HOI per `pham_vi_ap_dung` × 3 cấp (TW/BN/DP) = ≥9 record.
  - **Cần có sẵn:** [need: ≥3 TVV HOAT_DONG cover 3 LV (✗ chờ T-FR04-XXX); DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001); MAU_PHAN_HOI ≥12 (✗ chờ T-FR10-XXX); `cb_nv_tw_01` + `cb_nv_bn_01` + `cb_nv_dp_01` login OK]
  - **Spec:** FR-II-NEW-02 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1238-1243,1351-1355` (Hybrid model B)
  - **Output:** `output/qa-reports/round{N}/seed/hoi-dap/seed-checklist-fr02-002-mph-hybrid.md`

- 🟢 **T-FR02-003** Seed phiên TVN_BRIDGE escalate từ FR-13 → HOI_DAP `kenh_tiep_nhan='TVN_BRIDGE'`
  - **Kết quả:** Cần ≥2 HOI_DAP có `tu_van_nhanh_goc_id` FK về FR-13 phiên gốc.
  - **Cần có sẵn:** [need: ≥1 PHIEN_TV FR-13 state DA_KET_THUC (✗ chờ T-FR13-XXX); Cổng PLQG endpoint deploy (✗ chờ R7.6.3 infra); DN-side UI button "Chuyển sang TV thủ công" (✗ chờ FE deploy)]
  - **Spec:** `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:170,1046,1071` + FR-13 `srs-fr-13-tv-nhanh.md`
  - **Output:** `output/qa-reports/round{N}/seed/hoi-dap/seed-checklist-fr02-003-tvn-bridge.md`

### Group 2 — State lifecycle SM-HOIDAP (3 task)

- 🟢 **T-FR02-004** Workflow MOI → TIEP_NHAN → DA_PHAN_CONG → DANG_XU_LY (4 transition đầu chuỗi)
  - **Kết quả:** Cần PASS 4/4 transition + verify audit log entry mỗi chuyển trạng thái.
  - **Cần có sẵn:** [need: T-FR02-001 PASS ≥6 HD state MOI (✗ chờ); CB_NV cùng đơn vị login (✓); ≥3 NHT/TVV state HOAT_DONG cover ≥3 LV (✗ chờ T-FR04-XXX)]
  - **Spec:** FR-II-03 + FR-II-06 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:474,498,502,509,511` (DA_PHAN_CONG add)
  - **Output:** `output/qa-reports/round{N}/workflow/hoi-dap/workflow-test-report-fr02-004-tn-pc-xl.md`

- 🟢 **T-FR02-005** BR-FLOW-01 auto-transition `DA_TRA_LOI → CHO_PHE_DUYET` (tích checkbox "Đã trả lời")
  - **Kết quả:** Cần PASS — tích checkbox → auto SET CHO_PHE_DUYET (không cần bước "Trình") + CB PD nhận thông báo.
  - **Cần có sẵn:** [need: T-FR02-004 PASS ≥3 HD state DANG_XU_LY (✗ chờ); CB_NV được phân công login (✓); CB PD cùng cấp login (`cb_pd_tw_01` ✓)]
  - **Spec:** BR-FLOW-01 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1598-1600,559-583`
  - **Output:** `output/qa-reports/round{N}/workflow/hoi-dap/workflow-test-report-fr02-005-flow01-auto.md`

- 🟢 **T-FR02-006** Workflow phê duyệt + từ chối + đóng hồ sơ thủ công BR-FLOW-06 (CHO_PHE_DUYET → DA_DUYET / DANG_XU_LY → HOAN_THANH)
  - **Kết quả:** Cần PASS 3 path (duyệt OK / từ chối lý do ≥10 / đóng hồ sơ manual). Verify KHÔNG auto-close.
  - **Cần có sẵn:** [need: T-FR02-005 PASS ≥3 HD state CHO_PHE_DUYET (✗ chờ); CB PD cùng cấp `cb_pd_tw_01` (✓)]
  - **Spec:** FR-II-08 + BR-FLOW-04 + BR-FLOW-06 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1610-1630`
  - **Output:** `output/qa-reports/round{N}/workflow/hoi-dap/workflow-test-report-fr02-006-pd-tc-close.md`

### Group 3 — Phân công auto-filter 4 tiêu chí (2 task)

- 🟢 **T-FR02-007** FR-II-06 SCR-II-03 modal phân công CA_NHAN — verify auto-filter (lĩnh vực + đơn vị + workload + ho_ten sort)
  - **Kết quả:** Cần verify 4 tiêu chí filter + 10 record top. **Defer subtest sort/LIMIT — chờ BA confirm** (xem T-FR02-019).
  - **Cần có sẵn:** [need: T-FR02-004 PASS ≥3 HD state TIEP_NHAN (✗ chờ); ≥10 NHT/TVV HOAT_DONG cover 6 LV với workload variant (✗ chờ T-FR04-XXX advance-state); `cb_nv_tw_01` login (✓)]
  - **Spec:** FR-II-06 Step 5 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:470-473` (gốc — KHÔNG có sort/LIMIT) + `02-thu-tu-module.md:86,116,138,370` (derived — có sort/LIMIT)
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-007-phan-cong-auto-filter.md`

- 🟢 **T-FR02-008** FR-II-06 phân công TO_CHUC tư vấn (Tab Tổ chức) + ERR-PC-04/05/06 negative
  - **Kết quả:** Cần PASS 3 happy (chọn TC + TVV thuộc TC) + 3 negative (thiếu TC, TVV không thuộc TC, CA_NHAN truyền thừa TC).
  - **Cần có sẵn:** [need: ≥2 TO_CHUC_TV state HOAT_DONG (✗ chờ T-FR05-XXX); ≥3 TVV thuộc TC (✗ chờ T-FR04-XXX); T-FR02-001 PASS HD state TIEP_NHAN]
  - **Spec:** FR-II-06 ERR-PC-04/05/06 (test-plan §2.2)
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-008-phan-cong-tc.md`

### Group 4 — SLA cảnh báo (3 task)

- 🟢 **T-FR02-009** BR-SLA-01..02 — 4 mức cảnh báo BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG
  - **Kết quả:** Cần PASS 3 mức đầu (1/2/3). **Mức 4 defer chờ BA** — conflict 4 mức SRS vs 2 mức SCR-VIII-06.
  - **Cần có sẵn:** [need: T-FR02-004 PASS ≥4 HD state TIEP_NHAN (✗ chờ); CAU_HINH_SLA seeded `loai_yeu_cau=HOI_DAP` deadline=10 (✗ chờ T-FR10-XXX); time-travel DB access (✓)]
  - **Spec:** BR-SLA-01/02 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:265,992-998,1640-1642`
  - **Method:** Time-travel DB manipulation `ngay_tiep_nhan` ±N ngày
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-009-sla-4-muc.md`

- 🟢 **T-FR02-010** BR-SLA-03 cron 30 phút trigger + notification toggle on/off + BR-SLA-04 ngày lễ FR-VIII-29
  - **Kết quả:** Cần PASS 3 TC (cron trigger / notification toggle / ngày làm việc trừ ngày lễ).
  - **Cần có sẵn:** [need: T-FR02-009 PASS ≥3 HD state SAP_HET (✗ chờ); ≥1 NGAY_LE record FR-VIII-29 schema 5 trường (✗ chờ T-FR10-XXX); cron simulation access (✗ chờ Infra)]
  - **Spec:** BR-SLA-03/04 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:986,1646-1648` + `02-thu-tu-module.md:139`
  - **Method:** Cron simulation + email/in-app notification verify
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-010-sla-cron-ngayle.md`

- 🟢 **T-FR02-011** TC-EC-NO-AUTOCLOSE — verify BR-FLOW-06 KHÔNG auto-close sau 6 tháng (manual close only)
  - **Kết quả:** Cần PASS — time-travel +180 ngày, verify state DA_DUYET/CONG_KHAI giữ nguyên, không tự HOAN_THANH.
  - **Cần có sẵn:** [need: T-FR02-006 PASS ≥1 HD state DA_DUYET (✗ chờ); DBA query access cho time-travel (✗ chờ Infra/DBA)]
  - **Spec:** BR-FLOW-06 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1626-1630` (BA chốt 2026-05-05)
  - **Method:** Time-travel DB OR DBA query
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-011-no-autoclose.md`

### Group 5 — Công khai + Hủy công khai (2 task)

- 🟢 **T-FR02-012** Workflow công khai DA_DUYET → CONG_KHAI — API trực tiếp Cổng PLQG + 5 trường CR-01
  - **Kết quả:** Cần PASS — modal 5 trường, API push OK → SET CONG_KHAI + idempotency key + ERR-PD-04 negative (API fail → giữ DA_DUYET).
  - **Cần có sẵn:** [need: T-FR02-006 PASS ≥3 HD state DA_DUYET (✗ chờ); CB PD cùng cấp `cb_pd_tw_01` (✓); Cổng PLQG sandbox endpoint OK (✗ chờ Infra R7.6.3)]
  - **Spec:** BR-FLOW-05 + CR-01 + BR-EC-20 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1622-1624,722,1057`
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-012-cong-khai.md`

- 🟢 **T-FR02-013** Hủy công khai CONG_KHAI → DA_DUYET — verify `thoi_gian_dang_tai=NULL` + 4 trường còn lại giữ + ERR-PD-06
  - **Kết quả:** Cần PASS 2 happy (Hủy CK OK + Re-CK lại) + 1 negative (API gỡ Cổng fail → giữ CONG_KHAI).
  - **Cần có sẵn:** [need: T-FR02-012 PASS ≥1 HD state CONG_KHAI (✗ chờ); CB PD cùng cấp (✓)]
  - **Spec:** `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:658` (line 658: SET `thoi_gian_dang_tai=NULL` + `cong_khai=0`)
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-013-huy-ck.md`

### Group 6 — Auto-tạo FR-13 Kho QA (1 task)

- 🟢 **T-FR02-014** TC-XMOD-FR13-KHO-QA — verify `CHO_PHE_DUYET → DA_DUYET` AUTO insert KHO_QA `nguon=TU_DONG`
  - **Kết quả:** Cần PASS — verify KHO_QA record xuất hiện full-text search trên Cổng PLQG sau khi duyệt. **Defer chờ grep SRS FR-13** (xem T-FR02-019).
  - **Cần có sẵn:** [need: T-FR02-006 PASS ≥1 HD state DA_DUYET (✗ chờ); SRS FR-13 `srs-fr-13-kho-qa.md` field contract `kho_qa.nguon` (✗ chờ BA + grep)]
  - **Spec:** `01-tong-quan-nghiep-vu.md:87-97` (derived) + SRS FR-II-08 line 617 (KHÔNG có step INSERT KHO_QA — cần BA confirm)
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-014-xmod-kho-qa.md`

### Group 7 — Mẫu phản hồi Hybrid 2 tầng (2 task)

- 🟢 **T-FR02-015** FR-II-NEW-02 — CRUD MAU_PHAN_HOI 3 scope (TW_QUOC_GIA / BN_RIENG / DP_RIENG) qua MPH_CREATE_TW/BN/DP
  - **Kết quả:** Cần PASS 3 happy (CRUD 3 cấp đúng auto-fill `pham_vi_ap_dung`) + 4 negative (cross-cap, soft delete, optimistic lock, validation).
  - **Cần có sẵn:** [need: T-FR02-002 PASS ≥9 MPH (✗ chờ); `cb_nv_tw_01` + `cb_nv_bn_01` + `cb_nv_dp_01` login (✓); DM LINH_VUC_PL ≥6 (✗ chờ T-FR10-001)]
  - **Spec:** FR-II-NEW-02 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1238-1243,1351-1355` (Hybrid model B)
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-015-mph-crud.md`

- 🟢 **T-FR02-016** MPH_READ scope cross-cap dropdown chèn mẫu SCR-II-02 (TW xem TW only; BN xem TW+BN; DP xem TW+DP)
  - **Kết quả:** Cần PASS 3 scenario × 3 cấp = 9 verification matrix MPH_READ.
  - **Cần có sẵn:** [need: T-FR02-015 PASS ≥9 MPH (✗ chờ); T-FR02-004 PASS ≥3 HD state DANG_XU_LY (✗ chờ)]
  - **Spec:** Permission matrix §2.3 row MAU_PHAN_HOI — READ
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-016-mph-read-scope.md`

### Group 8 — Permission cross-cap (2 task)

- 🟢 **T-FR02-017** Permission matrix 11 role × 8 action HOI_DAP scope cross-cap (BR-AUTH-05 cùng cấp + BR-AUTH-08 don_vi_id)
  - **Kết quả:** Cần PASS 10 TC (3 happy + 6 negative cross-cap + 1 edge).
  - **Cần có sẵn:** [need: ≥3 account mỗi cấp TW/BN/DP với `_01`/`_02`/`_03` suffix (✓ users.csv); T-FR02-001..006 PASS HD đủ state đại diện (✗ chờ)]
  - **Spec:** BR-AUTH-05/08 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1546,1574-1576` + permission matrix §2.3
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-017-perm-cross-cap.md`

- 🟢 **T-FR02-018** BR-AUTH-10 lọc kép TVV/NHT/CG — chỉ thấy HD được phân công + audit trail INSERT-only
  - **Kết quả:** Cần PASS — TVV `huongcg` chỉ thấy HD assigned + audit log không cho UPDATE/DELETE.
  - **Cần có sẵn:** [need: T-FR02-007 PASS ≥3 HD assigned cho TVV/NHT (✗ chờ); TVV `huongcg` login (✓)]
  - **Spec:** BR-AUTH-10 `01-tong-quan-nghiep-vu.md:195-197` + BR-DATA-05 `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1592-1594`
  - **Output:** `output/qa-reports/round{N}/functional/hoi-dap/functional-test-report-fr02-018-perm-audit.md`

### Group 9 — BA escalate (1 task)

- 🟢 **T-FR02-019** BA escalate — clarify 3 spec inconsistency trước khi đóng module
  - **Kết quả:** Cần BA quote nguyên văn 3 line resolution.
  - **Cần có sẵn:** [need: BA available (✗); test-plan §2.1.0 FR-II-NEW-01 final status table prepared (✓)]
  - **3 câu hỏi BA:**
    1. **FR-II-NEW-01 DEPRECATED chính thức?** Quote line "xóa hẳn khỏi SRS v3.5" — vì line 449/829/1149/1174 vẫn reference.
    2. **Auto-filter Step 5 sort/LIMIT** — SRS gốc line 470-473 KHÔNG có. Derived `02-thu-tu-module.md:86,116,138,370` có "workload ASC + ho_ten ASC LIMIT 10". Authoritative nguồn?
    3. **BR-SLA-02 — 4 mức hay 2 mức?** SRS line 992-998 = 4 mức. SCR-VIII-06 (derived `02-thu-tu-module.md:114`) = 2 ngưỡng. + Confirm `kho_qa.nguon=TU_DONG` step ở FR-II-08 (line 617 không có).
  - **Spec:** test-plan §2.1.0 + review.md Critical 3 + Important "BR-SLA-02 conflict"
  - **Output:** `output/qa-reports/round{N}/ba-escalate/fr02-019-spec-inconsistency-resolution.md`

---

## Cross-module upstream dependency map

| Upstream task | Entity output | Downstream task | State predicate |
|---|---|---|---|
| `T-FR10-001` | DM LINH_VUC_PL ≥6 ACTIVE | T-FR02-001, T-FR02-002, T-FR02-015 | (✗ chờ) |
| `T-FR10-XXX` (NGAY_LE) | NGAY_LE FR-VIII-29 ≥1 schema 5 trường | T-FR02-010 | (✗ chờ) |
| `T-FR10-XXX` (SLA) | CAU_HINH_SLA `loai_yeu_cau=HOI_DAP` deadline=10 | T-FR02-009, T-FR02-010 | (✗ chờ) |
| `T-FR10-XXX` (MPH) | MAU_PHAN_HOI ≥12 baseline | T-FR02-002 | (✗ chờ) |
| `T-FR04-XXX` (TVV create) | ≥3 TVV HOAT_DONG cover 3 LV | T-FR02-002, T-FR02-004, T-FR02-007 | (✗ chờ) |
| `T-FR04-XXX` (TVV advance) | ≥10 NHT/TVV state DANG_HOAT_DONG với workload variant | T-FR02-007 | (✗ chờ) |
| `T-FR05-XXX` | ≥2 TO_CHUC_TV HOAT_DONG | T-FR02-008 | (✗ chờ) |
| `T-FR13-XXX` | ≥1 PHIEN_TV DA_KET_THUC | T-FR02-003 | (✗ chờ) |
| `R7.6.3` Infra | Cổng PLQG endpoint deploy sandbox | T-FR02-003, T-FR02-012 | (✗ chờ) |
| `BA escalate` | 3 spec resolution (NEW-01 + auto-filter + SLA) | T-FR02-007, T-FR02-009, T-FR02-014, T-FR02-019 | (✗ chờ) |

**Tổng upstream link:** 10 cross-module dependency edges.

---

## Note

> Note 2026-05-12 13:00:00 — todo.md generated từ test-plan.md v1.1 sau revise apply review.md REVISE (3 Critical: DA_PHAN_CONG add SM, auto-filter cite gốc, FR-II-NEW-01 status table). 19 task — 9 group bao trùm seed + state lifecycle + auto-filter + SLA + công khai + auto-Kho QA + MPH Hybrid + permission + BA escalate. Tất cả đang 🟢 chờ upstream T-FR10/T-FR04/T-FR05/T-FR13 + BA confirm.
