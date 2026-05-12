# TODO — FR-14 — Hợp đồng tư vấn

> **Module:** FR-14 Hợp đồng tư vấn (Nhóm X.3, SCR-X3-01) — CRUD thuần, KHÔNG phê duyệt.
> **Test plan:** [test-plan.md](test-plan.md) (v1.1, 48 TC, 22 P0 + 14 P1 + 12 P2)
> **Phân nhóm SRS update 2026-05-05:** Nhóm C — IMPACT only (cross-cutting `is_deleted` → `da_xoa`).
> **Sinh từ:** Reviser agent 2026-05-12 13:30:00 (apply review feedback REVISE).
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream

---

## Cross-module dependencies (upstream)

| Entity cần | State | Count | Module nguồn | Verify query |
|---|---|:-:|---|---|
| TVV (Bên B) | HOAT_DONG | ≥3 | FR-04 (T-FR04-XXX) | `GET /api/v1/tu-van-viens?trangThai=HOAT_DONG` |
| TCTV (tổ chức tư vấn) | HOAT_DONG | ≥1 | FR-04 (T-FR04-XXX) | `GET /api/v1/to-chuc-tu-van?trangThai=HOAT_DONG` |
| VU_VIEC | DA_TIEP_NHAN hoặc HOAN_THANH | ≥3 | FR-05 (T-FR05-XXX) | `GET /api/v1/vu-viecs?trangThai=HOAN_THANH` |
| DON_VI | active | ≥3 (TW + BN + DP) | FR-10 | `GET /api/v1/don-vis` |

---

## Tasks

### Group 1 — Seed HĐ

- 🟢 **T-FR14-001** Seed ≥6 Hợp đồng TV DANG_THUC_HIEN cover ma trận đơn vị × Bên B (TVV vs TCTV) `[need: ≥3 TVV HOAT_DONG (✗ chờ T-FR04-XXX); ≥1 TCTV HOAT_DONG (✗ chờ T-FR04-XXX); ≥3 DON_VI (✗ chờ T-FR10-XXX)]`
  - **Kết quả:** ⏳ chưa chạy — chờ seed upstream
  - **Acceptance:** ≥2 HĐ × mỗi đơn vị (TW + BN-BKH + DP-AG); ≥1 Bên B TVV + ≥1 Bên B TCTV; ≥1 mỗi status (DANG_THUC_HIEN, TAM_DUNG, HOAN_THANH, HUY)
  - **Output:** `seed-checklist-fr14-hdtv.md`

- 🟢 **T-FR14-002** Seed ≥3 HĐ liên kết VV (cover BR-HDTV-03 xóa guard) + ≥1 HĐ không có VV `[need: ≥3 VV state DA_TIEP_NHAN/HOAN_THANH (✗ chờ T-FR05-XXX); T-FR14-001 ✅]`
  - **Kết quả:** ⏳ chưa chạy — chờ T-FR14-001 + VV upstream
  - **Acceptance:** ≥1 HĐ với 1 VV link, ≥1 HĐ với 3 VV link, ≥1 HĐ không có VV
  - **Output:** append vào `seed-checklist-fr14-hdtv.md`

### Group 2 — CRUD HĐ với Bên B = TVV

- 🟢 **T-FR14-003** TC-CRUD-01/02/NEG-01/NEG-02/NEG-04/04/05/06 + TC-FILE-01 — CRUD HĐ với Bên B TVV (8 TC P0/P1) `[need: ≥3 TVV HOAT_DONG (✗ chờ T-FR04-XXX); T-FR14-001 ✅]`
  - **Kết quả:** ⏳ chưa chạy
  - **Test cases:** CRUD-01 (12 field), CRUD-02 (Bên A auto), CRUD-NEG-01/02/04 (ERR-HDTV-01/02/05), CRUD-04 (concurrency SEQ unique, script API parallel POST), CRUD-05/FILE-01 (upload), CRUD-06 (AUDIT_LOG)
  - **Output:** `functional-test-report-fr14-crud-tvv.md`

- 🟢 **T-FR14-004** TC-MTD-01/NEG-01/EDGE-01 + TC-TT-01/NEG-01/EDGE-01/02/03 — Accordion Mốc tiến độ + Thanh toán (8 TC) `[need: T-FR14-003 ✅ ≥1 HĐ TVV đã tạo]`
  - **Kết quả:** ⏳ chưa chạy
  - **Test cases:** MTD-01 (3 mốc 3 status), MTD-NEG-01 (validate), MTD-EDGE-01 (50+ mốc), TT-01 (progress 50%), TT-NEG-01 (SUM > giá trị), TT-EDGE-01 (SUM=giá trị), TT-EDGE-02 (SUM+1đ), TT-EDGE-03 (SUM=0)
  - **Output:** append vào `functional-test-report-fr14-crud-tvv.md`

### Group 3 — CRUD HĐ với Bên B = TCTV (Tổ chức tư vấn)

- 🟢 **T-FR14-005** TC-CRUD-01/02 với Bên B = TCTV — verify dropdown + entity binding khác TVV (3 TC P0) `[need: ≥1 TCTV HOAT_DONG (✗ chờ T-FR04-XXX); T-FR14-001 ✅]`
  - **Kết quả:** ⏳ chưa chạy
  - **Test cases:** Tạo HĐ Bên B TCTV → verify dropdown TCTV searchable, Bên A auto, mã HĐ format `HDTV-YYYYMMDD-SEQ` riêng. Verify entity binding khác `tu_van_vien_id` (có thể `to_chuc_tu_van_id`).
  - **Output:** `functional-test-report-fr14-crud-tctv.md`

### Group 4 — Cross-ref FR-06 Chi trả

- 🟢 **T-FR14-006** TC-CROSS-03 — Xóa HĐ đã có record Chi trả FR-06 → confirm behavior (block / null FK) **[SPEC-CLARIFY-HDTV-02]** `[need: ≥1 HĐ có record Chi trả FR-06 (✗ chờ T-FR06-XXX seed)]`
  - **Kết quả:** ⏳ chưa chạy — chờ FR-06 seed Chi trả + BA reply
  - **Method:** Tạo HĐ + Chi trả ref `hop_dong_tv_id` → DELETE HĐ → capture response (block 4xx hay 204 + null FK). Log evidence không tự kết luận PASS/FAIL.
  - **Output:** `functional-test-report-fr14-cross-module.md`

### Group 5 — Cross-ref FR-05 VV (FK direction)

- 🟢 **T-FR14-007** TC-LINK-VV-01 (Phương án A N:N) + TC-LINK-VV-01b (Phương án B 1:N) — test cả 2 model **[SPEC-CLARIFY-HDTV-04]** `[need: ≥3 VV HOAN_THANH (✗ chờ T-FR05-XXX); T-FR14-001 ✅]`
  - **Kết quả:** ⏳ chưa chạy
  - **Method:** Phương án A — link VV1+VV2+VV3 vào HĐ-A; verify accordion 3 row. Phương án B — link VV1 vào HĐ-A, rồi try link VV1 vào HĐ-B; verify reject (1:N) hoặc move (mất khỏi HĐ-A). Log evidence cả 2 escalate BA.
  - **Output:** `functional-test-report-fr14-link-vv.md`

- 🟢 **T-FR14-008** TC-LINK-VV-02a/02b/03 + TC-DEL-02/02b/03/04 — permission filter VV + xóa HĐ guard (7 TC) **[SPEC-CLARIFY-HDTV-04 sub VV soft-deleted]** `[need: T-FR14-007 chạy xong; ≥1 HĐ có VV link + ≥1 HĐ không VV (T-FR14-002 ✅)]`
  - **Kết quả:** ⏳ chưa chạy
  - **Test cases:** LINK-VV-02a (BR-AUTH-08 filter VV theo đơn vị), LINK-VV-02b (cross-link VV BN vào HĐ TW), LINK-VV-03 (bỏ link), DEL-02 (xóa HĐ có VV active), DEL-02b (VV soft-deleted edge), DEL-03 (xóa HĐ không VV → soft delete), DEL-04 (AUDIT_LOG DELETE)
  - **Output:** append vào `functional-test-report-fr14-link-vv.md`

### Group 6 — Search + Pagination + UI

- 🟢 **T-FR14-009** TC-SEARCH-01..06 + TC-PAG-01/02 + TC-UI-01/02 (10 TC) `[need: T-FR14-001 ✅ ≥20 HĐ trong DB (cần seed thêm 14 record nữa nếu T-FR14-001 chỉ 6)]`
  - **Kết quả:** ⏳ chưa chạy
  - **Test cases:** SEARCH-01..05 (keyword/filter/empty), SEARCH-06 (SQL inject + XSS), PAG-01 (20/page default), PAG-02 (boundary max 100 — API `?limit=101` reject), UI-01 (red badge ≤30 ngày), UI-02 (boundary 30/31)
  - **Output:** `functional-test-report-fr14-search-ui.md`

### Group 7 — Permission TVV xem HĐ embedded

- 🟢 **T-FR14-010** TC-PERM-TVV-01 — TVV login → tab "Lịch sử" SCR-IV-03 thấy chỉ HĐ chính mình **[SPEC-CLARIFY-HDTV-05]** `[need: T-FR14-003 ✅ ≥1 HĐ với Bên B TVV cụ thể (vd huongcg)]`
  - **Kết quả:** ⏳ chưa chạy — chờ BA confirm TVV/CG có quyền read HĐ embedded
  - **Method:** Login TVV `huongcg` → mở SCR-IV-03 tab "Lịch sử" → verify chỉ HĐ có `tu_van_vien_id = huongcg.id`; verify scope isolation (không thấy HĐ TVV khác).
  - **Output:** `functional-test-report-fr14-permission-tvv.md`

### Group 8 — Permission cross-unit + Auth + Audit + Cross-cutting

- 🟢 **T-FR14-011** TC-PERM-01..05 + TC-AUTH-01 + TC-AUDIT-01 + TC-CROSS-01 + TC-CROSS-02 (10 TC) `[need: T-FR14-003 ✅; accounts cb_nv_tw_01, cb_nv_bn_01, cb_nv_dp_01, cb_pd_tw_01, qtht_01, nht_01]`
  - **Kết quả:** ⏳ chưa chạy
  - **Test cases:** PERM-01 (CB_NV TW scope), PERM-02 (CB_NV BN-BKH cross-unit BR-AUTH-08), PERM-03 (CB_PD read-only), PERM-04 (NHT/DN 403), PERM-05 (QTHT all), AUTH-01 (session expire 401), AUDIT-01 (INSERT log), CROSS-01 (`da_xoa` schema regression), CROSS-02 (CR-01 negative — defer chờ BA)
  - **Output:** `functional-test-report-fr14-permission-audit.md`

### Group 9 — BA escalate (SPEC-CLARIFY consolidate)

- 🟢 **T-FR14-012** Soạn email/ticket BA gộp 5 SPEC-CLARIFY-HDTV-01..05 + evidence từ T-FR14-006/007/008/010 — **không block các task khác, chạy parallel** `[need: T-FR14-006/007/010 đã chạy xong để có evidence]`
  - **Kết quả:** ⏳ chưa chạy
  - **Nội dung:** (01) SM transition rules; (02) xóa HĐ có Chi trả guard; (03) HĐTV publish PLQG?; (04) FK direction N:N vs 1:N + Bên A readonly + VV soft-deleted count; (05) TVV/CG read HĐ embedded grant từ SRS FR nào?
  - **Output:** `spec-clarify-fr14-hdtv-batch.md` (gửi BA)

---

## Tổng hợp module

| Group | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ | ❌ | Task IDs |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| Seed | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-001, 002 |
| CRUD TVV | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-003, 004 |
| CRUD TCTV | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-005 |
| Cross-ref FR-06 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-006 |
| Cross-ref FR-05 (FK) | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-007, 008 |
| Search/UI | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-009 |
| Permission TVV | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-010 |
| Permission/Audit/Cross-cutting | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-011 |
| BA escalate | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | T-FR14-012 |
| **Tổng** | **12** | **12** | **0** | **0** | **0** | **0** | **0** | **0** |  |

---

## Tham chiếu

- Test plan: [test-plan.md](test-plan.md) v1.1
- Review: [review.md](review.md)
- SRS: `input/srs-v3/srs-fr-14-hop-dong-tv.md`
- Cross-cutting v3.5: `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`
- Permission matrix: `output/permission-matrix.md`
- Accounts: `input/users.csv`
