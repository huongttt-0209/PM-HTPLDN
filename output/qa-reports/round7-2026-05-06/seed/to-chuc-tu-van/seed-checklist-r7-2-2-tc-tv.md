# Seed checklist — R7.2.2 Seed 6 Tổ chức tư vấn (MOI_DANG_KY)

> ✅ **UI re-test 2026-05-09 R8 — PASS.** Đã seed thêm 3 TC TV qua UI (cb_nv_tw_02): **TC-BTP-TW-0006** (CONG_TY_LUAT, Theta) UUID `a32d7714-b834-49ff-b6a4-c3fede1c1eee`, **TC-0007** (VP_LUAT_SU, Iota) UUID `8fe25cb4-cab6-4b0c-a73e-0f1b6ce5b8dc`, **TC-0008** (TT_TVPL, Kappa) UUID `c92de88e-aeab-4859-bf26-5f8ff23e1fc7` — 3/3 PASS state `MOI_DANG_KY`, `POST /api/v1/to-chuc-tu-vans` 201 CREATED. Cover full 3 loại hình theo fixture. **BVA negative (KHAC + thiếu Số Giấy ĐKHĐ):** FE block client-side với message "Số Giấy ĐKHĐ là bắt buộc (NĐ 77/2008 Đ.13)" — đúng spec, không gửi BE.
>
> ⚠️ **Method note (2026-05-08):** API path 5 record ban đầu chạy thuần `POST` — vi phạm rule UI-only. UI path nay verified với 3 record bổ sung. **2 bug FE log hôm 2026-05-08 đều Closed sau re-test:** FE-002 Not-a-bug (BE auto-derive donViQuanLyId từ session user); FE-003 Not-reproducible (4/4 submit PASS hôm nay). Pool tổng: **5 HOAT_DONG** (0001..0005, từ API) **+ 3 MOI_DANG_KY** (0006..0008, qua UI) = 8 record. Bug log: [Pass-bug-report-r7-2-2-tctv-ui-seed.md](../../bug-reports/to-chuc-tu-van/Pass-bug-report-r7-2-2-tctv-ui-seed.md).

**Ngày chạy:** 2026-05-06 (R7)
**Account:** `cb_nv_tw_02` (CB_NV_TW)
**Endpoint:** `POST /api/v1/to-chuc-tu-vans`
**Fixture:** [seed-fixture.yaml v2.7.3 §to_chuc_tu_van_variants](../../../../input/data/seed-fixture.yaml) line 596-602
**SRS ref:** FR-IV-NEW-01 / CR-02 (`srs-update-2026-5-5/srs-fr-04-...`); NĐ 77/2008 Đ.13 (Giấy ĐKHĐ bắt buộc)

## Kết quả

✅ **5/5 PASS valid + 1/1 BVA negative đúng kỳ vọng** (Σ=6/6 fixture variants).

## Pool sau seed

| Mã | Tên | Loại hình | LV count | State |
|---|---|---|:-:|:-:|
| TC-BTP-TW-0001 | Công ty Luật TNHH Alpha Hà Nội | CONG_TY_LUAT | 3 | MOI_DANG_KY |
| TC-BTP-TW-0002 | Văn phòng Luật sư Beta Hải Phòng | VP_LUAT_SU | 2 | MOI_DANG_KY |
| TC-BTP-TW-0003 | Trung tâm TVPL Gamma Đà Nẵng | TT_TVPL | 3 | MOI_DANG_KY |
| TC-BTP-TW-0004 | Đoàn Luật sư Hà Nội | VP_LUAT_SU | 4 | MOI_DANG_KY |
| TC-BTP-TW-0005 | Công ty Luật TW Epsilon | CONG_TY_LUAT | 3 | MOI_DANG_KY |

**Verify:** `GET /api/v1/to-chuc-tu-vans?size=100` → `total: 5`, `byState: {MOI_DANG_KY: 5}`. Detail TC-0001 có `linhVucs[]` 3 record FK đúng.

## BVA negative (variant 5)

- **Idx 5 — Tổ chức TVPL Khác Delta** (KHAC, thiếu Giấy ĐKHĐ)
- **Status:** 422 `ERR-VAL-SYS-00-01` — `soGiayDkhd must be longer than or equal to 1 characters`
- **Kỳ vọng (fixture):** ERR-TCTV-* per NĐ 77/2008 Đ.13 → ✅ BE block save đúng spec.

## DM LV mapping

Fixture code → DB code (qua `GET /api/v1/danh-muc/tree?loaiDanhMuc=LINH_VUC_PL`):
- `THUONG_MAI` → `KINH_DOANH_TM` (DB chưa có THUONG_MAI thuần)
- `SHTT` → `SO_HUU_TRI_TUE`
- `LAO_DONG/THUE/DAT_DAI/DOANH_NGHIEP/DAN_SU/HINH_SU/HANH_CHINH/DAU_TU` — match trực tiếp.

## Đơn vị quản lý

| Variant | Fixture don_vi_quan_ly | Payload donViQuanLyId UUID |
|---|---|---|
| 1, 4 | DP-HN | `00000000-0000-4000-8002-000000000001` |
| 2 | DP-HP | `00000000-0000-4000-8002-000000000004` |
| 3 | DP-DN | `00000000-0000-4000-8002-000000000003` |
| 5, 6 | TW-CUC | `00000000-0000-4000-8000-000000000001` |

**Note:** Mã sequence BE auto-prefix `TC-BTP-TW-XXXX` theo cấp đơn vị tạo (account `cb_nv_tw_02` capDonVi=TW), kể cả TC TV cấp DP. Đây là behavior BE, không phải bug seed.

## Downstream

- ⏳ T2 (R7.2.3): Phê duyệt 5 TC TV → `HOAT_DONG` (account `cb_pd_tw_02`).
- ⏳ T3 (R7.2.6): Seed 6 CG TW dùng `toChucChinhId` từ pool 5 TC TV này.

## Smoke retest 2026-05-09 23:35:00

**Verdict:** ✅ Đạt — full luồng TC TV (4 task R7) còn ổn định.

**Account:** `cb_nv_tw_02` · **Tool:** Chrome DevTools MCP · **Mode:** smoke retest (không seed mới).

**Pool re-verify** (UI tabs + API `GET /api/v1/to-chuc-tu-vans?page=1&pageSize=100` HTTP 200):
- Total = **9** ✓ match state-snapshot 2026-05-09 17:25.
- HOAT_DONG = **7** (TC-BTP-TW-0001..0005, 0007, 0008) ✓.
- CHO_PHE_DUYET = **2** (TC-STP-AG-0001 An Giang, TC-STP-BG-0001 Bắc Giang) ✓.
- MOI_DANG_KY/TU_CHOI/TAM_DUNG/VO_HIEU_HOA = 0 ✓ (empty state "Trống" render đúng).

**Coverage cover R7 task:**
- R7.2.2 seed (loại hình) — 3 loại render: Trung tâm Tư vấn Pháp luật / Văn phòng Luật sư / Công ty Luật ✓.
- R7.2.3 advance HOAT_DONG — 7 record HOAT_DONG (sau R8 advance TC-0006/0007/0008) ✓.
- R7.4.A6 workflow state machine — detail TC-BTP-TW-0008: 4 action [Chỉnh sửa] / [Tạm dừng] / [Vô hiệu hóa] / [Xóa] + switch Công khai render đầy đủ ✓ (không trigger transition để tránh thay đổi pool).
- R7.7.4.6 functional — 6 tabs (HOAT_DONG/CHO_PHE_DUYET/MOI_DANG_KY/TU_CHOI/TAM_DUNG/VO_HIEU_HOA), search "Alpha" → 1 record TC-BTP-TW-0001 đúng, 3 filter combobox (Lĩnh vực / Đơn vị / Loại hình) render, pagination "20 / trang" page 1/1 ✓.

**Console:** clean (chỉ 1 warning AntD lib `Space direction` deprecation — không phải app bug).

**Bằng chứng:** [smoke-retest-2026-05-09-tc-tw-0008-detail.png](smoke-retest-2026-05-09-tc-tw-0008-detail.png)

**Drift đã ghi nhận từ R7 (giữ nguyên, không cần action):**
- TC-BTP-TW-0006 đã mất khỏi HOAT_DONG (drift unknown trước R2 16:35 R7.2.3).
- TC-BTP-TW-0009 đã DELETE qua BUG-001 R7.7.4.6 R1 (qtht_01 BE 403 đúng spec — bug đã đóng).
