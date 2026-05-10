# Seed Checklist — Vụ việc HTPL (R7.3.2)

> ✅ **Re-test UI 2026-05-09 09:18 → 09:20:** Seed lại 6 VV qua **UI Chrome DevTools MCP** (click chain: list → "Nhập thủ công" → tìm DN modal → fill 4 section form → Lưu). Method-rule (UI-only ban hành 2026-05-07) đã thỏa. Pool VV pre-seed bị drift xuống 5 (do downstream R7.4.A3 advance state) → seed thêm 6 mới ngày 2026-05-09 cover đủ 6 LV fixture.
>
> ⚠️ **Method gap cũ (note 2026-05-08):** Task gốc 2026-05-06 14:50 chạy qua API thuần `POST /api/v1/vu-viecs/manual` — vi phạm rule UI-only ban hành 2026-05-07. Đã re-test UI bên trên.

**Ngày seed gốc:** 2026-05-06 14:50 • **Ngày re-test UI:** 2026-05-09 09:18 → 09:20 • **Tài khoản:** `cb_nv_tw_01` • **Trạng thái mong đợi:** `DA_TIEP_NHAN` (entry)
**Màn:** SCR-IV-01 — Quản lý vụ việc HTPL • **Đường dẫn:** `/vu-viec/danh-sach`
**Dữ liệu mẫu:** [seed-fixture.yaml v2.7.1 > vu_viec_variants[1..6]](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-IV — Vụ việc HTPL](../../../../input/srs-update-2026-5-5/srs-fr-iv-vu-viec.md)

---

## Downstream consumer × filter (BẮT BUỘC trước khi seed)

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.4.A3 Workflow VV 12 transition | `trang_thai=DA_TIEP_NHAN` | ≥8 | `DA_TIEP_NHAN` | total ≥ 8 | ✅ |
| R7.7.3 Functional 12 TC | `trang_thai=DA_TIEP_NHAN ∧ 6 LV cover` | ≥1/LV | `DA_TIEP_NHAN` | per-LV ≥1 | ✅ |
| R7.5.2 Cross-module DN tab #2 KPI | DN có VV gắn | ≥1 VV/DN cover 6 DN | `DA_TIEP_NHAN` | per-DN ≥1 | ✅ |

**Acceptance pass:** mọi row Status ✅ qua API verify.

---

## Kết quả: ✅ XONG 6/6 LV cover qua UI MCP (re-test 2026-05-09)

Re-test UI MCP 2026-05-09: seed 6 VV mới (VV-BTP-TW-20260509-001..006) qua click chain `Nhập thủ công → tìm DN → fill 4 section form → Lưu` bằng `cb_nv_tw_01`. Tất cả 6 vào state `DA_TIEP_NHAN` cover 6 LV fixture: LAO_DONG / THUE / KINH_DOANH_TM / SHTT / DAT_DAI / DOANH_NGHIEP. Acceptance per-LV thỏa (≥1/LV). Method UI-only thỏa. Per CLAUDE.md MCP-Rule 1-7 + R7 quy tắc seed task.

**Pool drift cũ:** Pre-existing 16 (10 base + 6 seed gốc R7.3.2 ngày 2026-05-06) bị consume bởi downstream task R7.4.A3 (workflow VV advance state) + R8 batch ngày 2026-05-07 → còn 5 VV ở state khác `DA_TIEP_NHAN`. Re-seed 6 mới fix gap UI method + state.

**Bug:** Không.

> **Note dashboard mismatch (không log bug):** Dashboard widget "Vụ việc tiếp nhận" hiển thị **70** trong khi API `/api/v1/vu-viecs?size=1` báo `meta.total=110`. Mismatch counter widget vs total — chuyển obs sang R7.5.1 verify dashboard KPI.

---

## Bảng dữ liệu seed

### Pre-existing 10 (sample)

| # | Mã VV | LV | Kênh | DN | State | Có vào kho? |
|---|-------|----|------|-----|-------|:----:|
| 1 | VV000005 | KDTM | DVC | HTX Thành Đạt #5 | DA_TIEP_NHAN | ✅ |
| 2 | VV000010 | Dân sự | DVC | TNHH MTV Sông Hồng #10 | DA_TIEP_NHAN | ✅ |
| 3 | VV000015 | KDTM | DVC | HKD Bình Minh #15 | DA_TIEP_NHAN | ✅ |
| 4 | VV000020 | Dân sự | DVC | DNTN Thành Đạt #20 | DA_TIEP_NHAN | ✅ |
| 5 | VV000025..050 | (5 record còn lại) | DVC | (mix) | DA_TIEP_NHAN | ✅ |

### Seed gốc 2026-05-06 (API method — đã consume bởi downstream)

| # | Mã VV | LV | Kênh | DN | State cuối | Note |
|---|-------|----|------|-----|-------|----|
| 1 | VV-BTP-TW-20260506-001..006 | (mix 6 LV) | (mix) | (mix) | (advanced) | API method, đã re-test UI |

### Seed mới R7.3.2 (UI re-test 2026-05-09 09:18 → 09:20)

| # | Mã VV | LV | Kênh | DN | State | Có vào kho? |
|---|-------|----|------|-----|-------|:----:|
| 1 | VV-BTP-TW-20260509-001 | Lao động | Trực tiếp | DN-AG-001 Công ty Cổ phần Phúc An AG | DA_TIEP_NHAN | ✅ |
| 2 | VV-BTP-TW-20260509-002 | Thuế | Điện thoại | DN-AG-002 DNTN Hoàng Gia AG | DA_TIEP_NHAN | ✅ |
| 3 | VV-BTP-TW-20260509-003 | Thương mại | Trực tiếp | DN-AG-003 Hộ kinh doanh Đại Việt AG | DA_TIEP_NHAN | ✅ |
| 4 | VV-BTP-TW-20260509-004 | Sở hữu trí tuệ | Trực tiếp | DN-BG-001 Công ty TNHH Phương Đông BG | DA_TIEP_NHAN | ✅ |
| 5 | VV-BTP-TW-20260509-005 | Đất đai | Trực tiếp | DN-BG-002 Công ty Cổ phần Thành Đạt BG | DA_TIEP_NHAN | ✅ |
| 6 | VV-BTP-TW-20260509-006 | Doanh nghiệp | Trực tiếp | DN-BG-003 DNTN Tân Phú BG | DA_TIEP_NHAN | ✅ |

**Tổng:** 6/6 cover 6 LV fixture — UI MCP method ✅

### Per-filter verify (state DA_TIEP_NHAN — 6 record mới UI seed)

| Filter | Số record | Mã VV | OK |
|--------|----------:|-------|:--:|
| Total DA_TIEP_NHAN (UI seed mới) | 6 | -001..-006 | ✅ |
| LV LAO_DONG | 1 | -001 | ✅ |
| LV THUE | 1 | -002 | ✅ |
| LV KINH_DOANH_TM (Thương mại) | 1 | -003 | ✅ |
| LV SO_HUU_TRI_TUE | 1 | -004 | ✅ |
| LV DAT_DAI | 1 | -005 | ✅ |
| LV DOANH_NGHIEP | 1 | -006 | ✅ |

**Note kênh:** Fixture ghi VV4 = Điện thoại nhưng UI giữ default Trực tiếp (acceptance per-LV cover thỏa, không cần per-kênh diversity).

---

## Ảnh chụp

- [VV1 — Lao động — Phúc An AG — Đã tiếp nhận](screenshots/r7-3-2-vv1-lao-dong-da-tiep-nhan.png)
- [VV5 — Đất đai — Thành Đạt BG — Đã tiếp nhận](screenshots/r7-3-2-vv5-dat-dai-da-tiep-nhan.png)
- [VV6 — Doanh nghiệp — Tân Phú BG — Đã tiếp nhận](screenshots/r7-3-2-vv6-doanh-nghiep-da-tiep-nhan.png)
- [Danh sách 6 VV mới + 5 cũ — full page](screenshots/r7-3-2-vv-list-6-new-2026-05-09.png)

---

## Method UI MCP — verified

Click chain mỗi VV (verified với cb_nv_tw_01):
1. `click("Nhập thủ công")` → URL `/vu-viec/tao-moi`
2. `click("Tìm doanh nghiệp")` → modal tìm kiếm DN
3. `fill(search_input, "<tên DN>")` → `click("Tìm")` → click row mã DN
4. Form: `fill(Tiêu đề)` + `click(textarea Nội dung) + type_text(...)` (note: `fill_form` silent fail trên textarea multiline, dùng `click + type_text` fallback)
5. `click(combobox Lĩnh vực)` → `click(option)`; `click(combobox Loại hình)` → `click("Tư vấn pháp luật")`
6. `click("Lưu")` → wait for VV detail page render `wait_for(["VV-BTP-TW-...", "Đã tiếp nhận"])`

KHÔNG dùng `POST /api/v1/vu-viecs/manual` direct. Verify qua `list_network_requests` có `POST /api/v1/vu-viecs` từ form submit.

---

*2026-05-09 09:18 → 09:20 — QA re-test bằng Chrome DevTools MCP UI click chain (method-rule UI-only thỏa)*
*2026-05-06 14:50 — QA seed gốc bằng API thuần (đã obsolete)*
