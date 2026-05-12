# TODO — FR-12 — Tư vấn pháp luật chuyên sâu (rename v3.5)

> **Module:** L (LỚP 3, GIAO DỊCH LÕI, #⑧ thứ tự seed) — Tư vấn pháp luật chuyên sâu (rename từ "Tư vấn chuyên sâu" v3.5)
> **Test plan:** [test-plan.md](test-plan.md) (Revised 2026-05-12 13:00:00, 50 TC, 7 FR + cross-module)
> **SRS active:** `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md` (1617 dòng v3.5)
> **Tạo:** 2026-05-12 13:00:00

## Icon meaning

- 🟢 Ready — đủ dep, có thể chạy ngay
- ⏳ Pending — chờ upstream task hoặc resource
- 🚫 Block — block hard (data/permission/env/spec mâu thuẫn)
- ⚠️ Partial — chạy nhưng có defect / sai spec
- ✅ Done — PASS clean
- ❌ Fail — FAIL có bug log

## Cross-module upstream dependencies (LỚP 1→2 seed chain)

| Entity upstream | State cần | Verify command (MCP) | Status |
|---|---|---|:-:|
| `TU_VAN_VIEN` (CG role) `trang_thai=HOAT_DONG` ≥3 records cover ≥2 LV | HOAT_DONG (v3.5 rename) | `list_network_requests` filter `/api/v1/tu-van-viens?loai_tvv=CG&trang_thai=HOAT_DONG` | ✗ chờ T-FR04-XXX |
| `DOANH_NGHIEP` ≥3 records `trang_thai=HOAT_DONG` cùng đơn vị test | HOAT_DONG | `/api/v1/doanh-nghieps?trang_thai=HOAT_DONG` | ✗ chờ T-FR07-XXX |
| `DANH_MUC` loại `LINH_VUC_PL` ≥2 records | (active) | `/api/v1/danh-muc?loai=LINH_VUC_PL` | ✗ chờ T-FR10-001 |
| `DON_VI` ≥1 record cấp DP (mặc định Sở TP) | (active) | `/api/v1/don-vi?cap=DP` | ✗ chờ T-FR10-002 |
| `CAU_HINH_SLA` row "TVCS phân công 2 ngày LV" | configured | `/api/v1/cau-hinh-sla?key=tvcs_phan_cong` | ✗ chờ T-FR10-003 |
| `CONG_PLQG_API_KEY` `cong_plqg_dn_test` provisioned | active | curl inbound `X-API-Key` thử 200 | ✗ chờ T-FR16-XXX |

---

## Task list — FR-12 (12 task chính)

- 🟢 **T-FR12-001** Seed YC TVCS thủ công CB NV (entry state TIEP_NHAN)
  - **Kết quả:** Chờ chạy. 6 variants theo `seed-fixture.yaml::tu_van_cs_variants[1..6]`, ≥1 record/LV.
  - **Cần có sẵn:** [need: ≥3 CG HOAT_DONG (✗ chờ T-FR04-XXX); ≥3 DN HOAT_DONG (✗ chờ T-FR07-XXX); DM LINH_VUC_PL (✗ chờ T-FR10-001); DON_VI DP (✗ chờ T-FR10-002)]
  - **Output:** seed-checklist-FR-12.md (GĐ 1)

- 🟢 **T-FR12-002** State lifecycle TVCS — walk full 10 transition SM-TVCS qua UI (advance state cho seed downstream)
  - **Kết quả:** Chờ chạy. Walk TIEP_NHAN → PHAN_CONG → DANG_TU_VAN → HOAN_THANH → CHO_PHE_DUYET → DA_DUYET + nhánh HUY (PHAN_CONG→HUY, DANG_TU_VAN→HUY) + nhánh từ chối CB PD. Per-transition verify DB state + TB + AUDIT_LOG.
  - **Cần có sẵn:** [need: T-FR12-001 hoàn tất (entry state ≥3 records TIEP_NHAN ✗); CB_PD_DP login OK; CG login OK]
  - **Output:** workflow-test-report-FR-12.md (GĐ 2), 10 sub-step cover TVCS-002a..f

- 🟢 **T-FR12-003** Functional TC TVCS-001..010 — CRUD + công khai chuyên trang (BR-PUBLIC-01-TVCS, BR-PUBLIC-02, BR-PUBLIC-03)
  - **Kết quả:** Chờ chạy. Bao gồm TVCS-002a..f (6 sub-TC transition split per review), TVCS-006/007/008 công khai, TVCS-009 BR-FLOW-04, TVCS-010 auto-save 30s.
  - **Cần có sẵn:** [need: ≥3 TVCS records mỗi state (TIEP_NHAN/PHAN_CONG/DANG_TU_VAN/HOAN_THANH/CHO_PHE_DUYET/DA_DUYET) — phụ thuộc T-FR12-002; endpoint `/trao-doi-nhap` cho TVCS-010 (✗ §7 Open #6 chờ Dev BE)]
  - **Output:** functional-test-report-FR-12-tvcs-crud.md

- 🟢 **T-FR12-004** Functional TC TVCS-SEARCH-001..003 — FTS unaccent + filter 6 chiều + sanitize
  - **Kết quả:** Chờ chạy. Verify BR-DATA-08 (unaccent "tu van" match "tư vấn"), ERR-TVCS-TK-01, BR-EC-13 sanitize.
  - **Cần có sẵn:** [need: ≥10 TVCS records cover 2-3 LV để FTS có dataset (✗ phụ thuộc T-FR12-001+002)]
  - **Output:** functional-test-report-FR-12-tvcs-search.md

- 🟢 **T-FR12-005** Inbound API TVCS — UC149 (TVCS-API-001..007) + BR-ROUTE-TVCS-01 3 case + boundary 100MB
  - **Kết quả:** Chờ chạy. TVCS-API-007 boundary tổng 100MB (10 file × 10MB + 1 thừa) — thêm per review. Verify `nguon=CONG_PLQG`, idempotency `ma_noi_dung_cong`.
  - **Cần có sẵn:** [need: API key `cong_plqg_dn_test` provisioned (✗ chờ T-FR16-XXX); DN MST tồn tại để BR-ROUTE-TVCS-01 default lookup (✗ chờ T-FR07-XXX)]
  - **Output:** functional-test-report-FR-12-tvcs-inbound-api.md

- 🟢 **T-FR12-006** Functional TC HSPL-001..005 — CRUD HSPL + NHT BR-AUTH-10 lọc kép + Export 10k
  - **Kết quả:** Chờ chạy. HSPL-002/003 cover NHT in/out scope; case boundary (VV chuyển CG, VV đóng) defer §7 ambiguity #7.
  - **Cần có sẵn:** [need: ≥3 DN HOAT_DONG (✗ chờ T-FR07-XXX); ≥1 VV phân công NHT có DN scope (✗ chờ T-FR09-XXX); NHT login OK]
  - **Output:** functional-test-report-FR-12-hspl-crud.md

- 🟢 **T-FR12-007** Inbound API HSPL — UC151 (HSPL-API-001..003) + upsert DN theo MST
  - **Kết quả:** Chờ chạy. HSPL-API-003 file mã độc → ERR-FILE-02 + audit row.
  - **Cần có sẵn:** [need: API key provisioned (✗ chờ T-FR16-XXX); sample DN MST cũ/mới để test upsert (✗ chờ T-FR07-XXX)]
  - **Output:** functional-test-report-FR-12-hspl-inbound-api.md

- 🟢 **T-FR12-008** Functional TC TLPL-001..006 — TLPL CRUD + công khai TRỰC TIẾP BR-FLOW-07 ⭐ + permission lọc kép
  - **Kết quả:** Chờ chạy. TLPL-002 happy publish KHÔNG cần approve (BR-FLOW-07). **TLPL-006 negative permission** thêm per review: CG (`cg_01`) / NHT (`nht_01`) / DN qua API publish → 403.
  - **Cần có sẵn:** [need: ≥1 TVCS bất kỳ state (✗ phụ thuộc T-FR12-001); CB_NV_DP + CG + NHT login OK; §7 #5 BA confirm modal required fields TLPL]
  - **Output:** functional-test-report-FR-12-tlpl-crud.md

- 🟢 **T-FR12-009** Inbound API đánh giá chất lượng — UC153 (DGCL-API-001..004) + idempotency `hanh_dong=GUI_LAI`
  - **Kết quả:** Chờ chạy. Verify cập nhật điểm TB CG sau insert; GUI_LAI 2 lần không ghi đè.
  - **Cần có sẵn:** [need: ≥1 TVCS DA_DUYET có CG đã hoàn thành (✗ phụ thuộc T-FR12-002); API key provisioned (✗ chờ T-FR16-XXX)]
  - **Output:** functional-test-report-FR-12-dgcl-inbound-api.md

- 🟢 **T-FR12-010** Outbound API metadata-only — FR-XII-13 CROSS-001 (public, no auth) + field-list expose/hide
  - **Kết quả:** Chờ chạy. EXPOSE: `ma_noi_dung`, `doanh_nghiep.ten`, `linh_vuc_pl.ten`, `tom_tat`, `ngay_hoan_thanh`, `thoi_gian_dang_tai`, `anh_dai_dien`. HIDE: `noi_dung_tu_van`, `ket_qua`, `tai_lieu_dinh_kem`, `chuyen_gia_id`, `nguoi_phe_duyet_id`, `don_vi_id`, audit fields.
  - **Cần có sẵn:** [need: ≥3 TVCS DA_DUYET đã bật `cong_khai=1` (✗ phụ thuộc T-FR12-003 TVCS-006)]
  - **Output:** functional-test-report-FR-12-cross-module.md (CROSS-001)

- 🟢 **T-FR12-011** Rename v3.5 impact regression — CROSS-002..004 + breadcrumb / entity / enum sync
  - **Kết quả:** Chờ chạy. CROSS-002 API body KHÔNG có `hinh_thuc_tv`; CROSS-003 UI breadcrumb + page title = "Tư vấn pháp luật chuyên sâu"; CROSS-004 dropdown CG filter `trang_thai=HOAT_DONG` (rename từ `DANG_HOAT_DONG`).
  - **Cần có sẵn:** [need: app deploy v3.5 stable; FR-04 SM-TVV enum rename HOAT_DONG đã apply (✗ chờ T-FR04-XXX advance state task)]
  - **Output:** functional-test-report-FR-12-cross-module.md (CROSS-002/003/004)

- 🟢 **T-FR12-012** Permission CG lọc kép + matrix toàn role × entity
  - **Kết quả:** Chờ chạy. Verify CG chỉ thấy TVCS được phân công (BR-AUTH-08 + assignment scope); NHT lọc kép HSPL (BR-AUTH-10); CB_PD cùng cấp (BR-AUTH-05). TVCS-005 negative CB_PD_BN duyệt DP → 403.
  - **Cần có sẵn:** [need: ≥3 CG được phân công TVCS khác đơn vị; ≥1 CB_PD mỗi cấp TW/BN/DP login OK; §7 #8 BA confirm TW phân công CG cross-unit]
  - **Output:** functional-test-report-FR-12-permission.md

---

## Tiến độ tổng

| Trạng thái | Count |
|---|---:|
| 🟢 Ready (chờ chạy round mới) | 12 |
| ⏳ Pending upstream | 0 |
| 🚫 Block | 0 |
| ⚠️ Partial | 0 |
| ✅ Done | 0 |
| ❌ Fail | 0 |
| **Tổng task** | **12** |

> **Lưu ý:** mọi task hiện 🟢 vì test plan vừa generate. Khi seed upstream chưa xong, marker `[need: ...]` vẫn `(✗ ...)` — hook `auto-rescan-todo.py` sẽ giữ trạng thái 🟢 (sẵn sàng khởi động seed) nhưng tester cần verify state-snapshot trước khi flip ⏳→🟢 cho TC functional.

## Reference

- [test-plan.md](test-plan.md) — 50 TC, mapping FR ↔ TC ↔ BR §4.1
- [review.md](review.md) — REVISE 2026-05-12 14:43:59 (12 gap + 10 suggestion, 8/12 applied)
- [`input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md`](../../../input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md)
- [`input/flow-module.md`](../../../input/flow-module.md) §FR-12 + Phụ lục 2 preset
- [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) `tu_van_cs_variants[1..6]`
- [`output/permission-matrix.md`](../../../output/permission-matrix.md)
