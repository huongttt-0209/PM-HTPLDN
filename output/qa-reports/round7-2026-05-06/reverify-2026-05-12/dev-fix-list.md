# Danh sách bug cần dev fix — Sau R26 reverify 2026-05-18 14:35:00 (Chrome DevTools MCP UI-first)

> **R26 update (2026-05-18 14:35:00):** Re-verify 2 bug Open R25 bằng MCP fresh isolated context `r26-bug1-pcwrn-cbnvtw01` (reuse cho cả 2 bug). **1 đóng mới**: BUG-VV-FN-LICHSU-01 — FE đã FIX option (b) per khuyến nghị R25: legacy VV-002 API vẫn trả `[UPDATE, UPDATE, CREATE]` (BE chưa migrate) NHƯNG UI timeline NAY render đủ 3 entries label tiếng Việt "Yêu cầu bổ sung"/"Kiểm tra"/"Tạo mới" — FE derive label theo `duLieuMoi.trangThai`. Fresh VV-001 vẫn canonical "Yêu cầu bổ sung"/"Tạo vụ việc" ✓. Cả 2 path PASS → **CLOSED-VERIFIED**. **1 unchanged**: BUG-VV-PC-WRN-01 — modal Phân công empty state vẫn thiếu override mechanism per SRS line 781 (DOM probe `itemCount: 0`, `dialogButtons: ["", "Hủy", "Xác nhận"]`, `overrideHints: []`).

> **R25 update (2026-05-16 10:30:00):** Re-verify 3 bug Open R24 bằng MCP fresh isolated context (3 context riêng `r25-bug1-dg013-cbnvdp02`, `r25-bug2-pcwrn-cbnvtw01`, reuse cho bug 3). **1 đóng mới**: BUG-FUNC-DG-013 — FE đã FIX surface spec message + error code ✓ (page `/403` render "Bạn không có quyền xem kết quả đánh giá này" + "Mã lỗi: ERR-DG-10" + role text); BE giữ FIX `ERR-DG-10` 3/3 endpoint. Cả BE + FE align spec → **CLOSED-VERIFIED**. **2 unchanged**: (a) BUG-VV-PC-WRN-01 — modal Phân công empty state thiếu override mechanism per SRS line 781 (DOM probe `hasOverrideButton: false`, `itemCount: 0`, `dialogButtons: ["", "Hủy", "Xác nhận"]`); (b) BUG-VV-FN-LICHSU-01 — FE i18n FIX cho fresh data giữ vững (VV-BTP-TW-20260514-001 timeline render "Yêu cầu bổ sung"/"Tạo vụ việc"); legacy VV-002 `[UPDATE, UPDATE, CREATE]` vẫn chỉ render 1 entry "Tạo mới" (FE hide 2 UPDATE).

> **R24 update (2026-05-15 11:10:00):** Verify lại 3 bug Open bằng MCP fresh isolated context. **2 progress**: (1) BUG-FUNC-DG-013 — BE đã FIX hoàn toàn ✓ (ERR-DG-10 + đúng spec message), chỉ còn FE generic /403 page. (2) BUG-VV-FN-LICHSU-01 — FE đã FIX i18n cho data fresh ✓ (timeline render label tiếng Việt "Yêu cầu bổ sung"/"Tạo vụ việc"/"Phân công"/"Kiểm tra"); residual chỉ legacy VV chưa migrate enum. **1 unchanged**: BUG-VV-PC-WRN-01 — chưa fix, modal Phân công empty state vẫn thiếu override mechanism per SRS line 781.

**Tổng cộng: 1 bug Open** (R26 đóng thêm 1: BUG-VV-FN-LICHSU-01 FE FIX option (b)). Lịch sử closed: R23-reverify đóng BUG-E2E-S4-011. R25 đóng BUG-FUNC-DG-013. R26 đóng BUG-VV-FN-LICHSU-01.

| Phân loại | Số lượng |
|---|:-:|
| P0 Critical | 0 |
| P1 Major | 0 |
| P2 Medium | 1 (BUG-VV-PC-WRN-01 — modal override mechanism, dev FE+BE — R26 unchanged) |
| P3 Minor | 0 |

### R26 reverify summary

| Bug ID | R25 status | R26 status | Δ progress |
|---|---|---|---|
| BUG-VV-PC-WRN-01 | Open Minor P2 (no override mechanism) | Open Minor P2 (no override mechanism) | Unchanged |
| BUG-VV-FN-LICHSU-01 | Open Minor P3 (FE i18n fresh ✓, legacy hide UPDATE) | **Closed-verified** ✅ (FE FIX option (b) derive label theo `duLieuMoi.trangThai`) | **FE FIX done — Closed** |

### R25 reverify summary (kept for history)

| Bug ID | R24 status | R25 status | Δ progress |
|---|---|---|---|
| BUG-FUNC-DG-013 | Open Minor P3 (BE FIX ✓, FE generic /403) | **Closed-verified** ✅ (BE + FE align spec) | **FE FIX done — Closed** |
| BUG-VV-PC-WRN-01 | Open Minor P2 (no override mechanism) | Open Minor P2 (no override mechanism) | Unchanged |
| BUG-VV-FN-LICHSU-01 | Open Minor P3 (FE FIX i18n fresh ✓, legacy hide UPDATE) | Open Minor P3 (giữ vững, legacy backfill chưa fix) | Unchanged |

---

## 1. Bảng 1 bug Open cần dev fix

| # | Bug ID | Module | Sev | P | Ai làm | Tóm tắt fix | File bug report |
|:-:|---|---|:-:|:-:|:-:|---|---|
| 1 | BUG-VV-PC-WRN-01 | Vụ việc | Minor | P2 | Dev FE + BE | **R26 re-replicate — unchanged Open.** MCP fresh `cb_nv_tw_01` mở VV-QA-R7-PRIVACY-DNAG002 (LV Doanh nghiệp DANG_KIEM_TRA) → modal Phân công DOM probe: dialog có radio Cá nhân/Tổ chức + combobox + textarea + 2 button Hủy/Xác nhận. Force search `XXKHONGMATCH99` → listbox empty message "Trống — Không tìm thấy đối tượng phù hợp lĩnh vực — Liên hệ QTHT để mở rộng lĩnh vực TVV/NHT, hoặc chọn vụ việc khác." `itemCount: 0`, `dialogButtons: ["", "Hủy", "Xác nhận"]`, `overrideHints: []`. BE LV-locked enforced, KHÔNG có "tìm thủ công" path per `srs-fr-05-vu-viec.md:781`. Dev FE+BE bổ sung mechanism (button/toggle/clear-LV/dropdown unfiltered). | [bug-report-flow-vu-viec.md](../bug-reports/vu-viec/bug-report-flow-vu-viec.md) |

---

## 2. Bug đã Closed R20+R22+R22-verify2+R23-reverify+R25+R26 (12 bug)

| Bug ID | Module | Verify evidence |
|---|---|---|
| ~~BUG-BC-PDF-NOT-SUPPORTED~~ | Báo cáo | R20 — 10/10 enum hợp lệ trả 200 + binary PDF |
| ~~BUG-VV-R19c-001~~ | Vụ việc | R20 — TVV header có button [Cập nhật KQ] + [Trình PD] state DANG_XU_LY |
| ~~BUG-BE-TVCS-R19c-010~~ | TVCS | R20 — Upload PDF 201 + `trangThaiQuet=SACH` |
| ~~BUG-HDTV-037 + 038~~ | HĐ tư vấn | R20 — "Đang thực hiện" + pagination "mục" |
| ~~BUG-E2E-S4~~ | Cross-cutting | R20 — DN portal có button "Gửi yêu cầu HTPL" |
| ~~BUG-E2E-S5~~ | Cross-cutting | R20 — Accordion label "Đơn vị quản lý" |
| ~~BUG-CHITRA-010~~ | Chi trả | R22 — Fresh DKT→YCBS HSCT-HDSD-001 16:41 → `ngayYeuCauBoSung` set NOW khớp lichSu YCBS timestamp. |
| ~~BUG-BC-DATA-SCOPE-LEAK~~ | Báo cáo | **R22-verify2 17:10** — Fresh probe 3 isolatedContext TW/BN/DP: 4/4 endpoint scope đúng (TW=34/5/209M/9 vs BN BTC=0/0/12.6M/0 vs DP Sở BG=1/0/103.4M/0). BE đã wire dataScopeMiddleware. |
| ~~BUG-VV-FN-PC-INACTIVE-01~~ | Vụ việc | **R22-verify2 17:13** — POST /phan-cong TVV inactive → 422 + message "ERR-PC-02: Đối tượng được chọn đã bị vô hiệu hóa". State VV giữ DANG_KIEM_TRA, không advance. |
| ~~BUG-E2E-S4-011~~ | Cross-cutting | **R23-reverify 2026-05-14 01:05** — Fresh probe MCP DN `9999999990`: modal "Gửi yêu cầu hỗ trợ pháp lý" → dropdown "Loại hình hỗ trợ" render 6 options đúng spec. FE đã align với FR-10 source-of-truth `LOAI_HINH_HO_TRO`. |
| ~~BUG-FUNC-DG-013~~ | Đánh giá HQ | **R25 2026-05-16 10:15:00** — Fresh probe `cb_nv_dp_02` STP-BG cross-cơ quan: API 3/3 endpoint `/ke-hoach-danh-gias/{id}` + `/bao-cao` + `/ket-quas` trả 403 + `{code: "ERR-DG-10", message: "Bạn không có quyền xem kết quả đánh giá này"}` đúng spec `srs-fr-08-danh-gia.md:786`. FE auto-redirect `/403` render đúng "Bạn không có quyền xem kết quả đánh giá này" + "Mã lỗi: ERR-DG-10" + role. Cả BE + FE align spec. |
| ~~BUG-VV-FN-LICHSU-01~~ | Vụ việc | **R26 2026-05-18 14:35:00** — Fresh `cb_nv_tw_01`: VV-001 (`4a1a6889-...`) API trả `[YEU_CAU_BO_SUNG, TAO_VV]` canonical, UI render "Yêu cầu bổ sung" + "Tạo vụ việc" ✓. Legacy VV-002 (`33b5a612-...`) API vẫn `[UPDATE, UPDATE, CREATE]` (BE chưa migrate) NHƯNG UI render đủ 3 entries label tiếng Việt "Yêu cầu bổ sung" + "Kiểm tra" + "Tạo mới" — FE đã thêm fallback derive theo `duLieuMoi.trangThai` cho enum UPDATE (option (b) khuyến nghị R25). Cả 2 path PASS. |

**File đã rename `Pass-` prefix:** TVCS-R16 / HDTV-7-14 / E2E-seam-gaps / E2E-S4-loai-hinh-empty / R22-fr-vi-10 (R25) / **r7-7-3-functional-vu-viec (R26 — sau khi đóng LICHSU-01)**.

---

## 3. Bug loại trừ — chờ phase tích hợp API ngoài (4 bug)

| Bug ID | Module | Sev | External dependency |
|---|---|:-:|---|
| BUG-CHITRA-008 | Chi trả | Medium | DVC LGSP gateway sandbox |
| BUG-API-001 | Cross-cutting | Major | mTLS cert client + sandbox staging |
| BUG-API-002 | Cross-cutting | Critical | 8/9 cặp outbound API publish |
| BUG-FUNC-TVN-008 | Tư vấn nhanh | Minor | Cổng PLQG CMS proxy |

---

## 4. Codex second-opinion review (2026-05-13 17:25:00 — kept for historical context, R23-reverify update)

| # | Bug | Codex verdict R22 | R23 actual outcome | Recommended fix path |
|:-:|---|---|---|---|
| 1 | ~~BUG-E2E-S4-011~~ | Partial — gốc SRS mâu thuẫn | **CLOSED R23** — FE đã align FR-10 `LOAI_HINH_HO_TRO`, BA decision bypass (FE chọn theo NotebookLM khuyến nghị). | — |
| 2 | BUG-FUNC-DG-013 | Real bug — SRS không mơ hồ | **Partial CLOSED R23** — VPD gate fix đúng (`donViId = coQuanDuocDanhGiaId` exception đã wire); còn Minor wording error code. | Dev BE đổi response 403 cross-cơ quan mapping → `ERR-DG-10` |
| 3 | BUG-VV-PC-WRN-01 | Real bug Minor | **Vẫn Open R23** | **Khuyến nghị BE thêm endpoint search TVV active không lọc LV** (path b) — contract rõ hơn path (a) FE toggle re-fetch dễ lặp 422 |
| 4 | BUG-VV-FN-LICHSU-01 | Real bug — không phải wording-only | **Partial progress R23** — alias `TRINH_PD` đã sửa (12→13/18 enum) | BE emit service `vu-viec`: gom 5 enum missing vào **1 PR**; backfill 4 legacy tách PR riêng |

**Tóm tắt R23-reverify:** 1 bug đóng thực (BUG-E2E-S4-011), 1 Partial CLOSED severity-downgrade (BUG-FUNC-DG-013 Major P1 → Minor P3), 2 bug vẫn Open chờ dev.

---

## 5. R23-verify3 seed walk update (2026-05-14 13:45:00)

| # | Bug | R23-verify3 pre-seed | R23-verify3 fresh seed (13:45) | Action dev |
|:-:|---|---|---|---|
| 1 | BUG-FUNC-DG-013 | Minor P3 wording residual (verified 12:30) | Không thay đổi — không cần seed | Dev BE đổi error code mapping cross-cơ quan FR-VI-10 → ERR-DG-10 + FE add domain-specific 403 page |
| 2 | BUG-VV-PC-WRN-01 | Minor P2 (verified 12:45 cb_nv_dp_01 LV Doanh nghiệp) | **Replicate trên fresh VV2 LV Đất đai** với meaningful keyword `hương tvv1` (TVV HOAT_DONG ngoài LV) — empty + message hint chỉ 2 path (QTHT/đổi vụ), không có "tìm thủ công" | Dev FE+BE bổ sung override mechanism per `srs-fr-05-vu-viec.md:781` |
| 3 | BUG-VV-FN-LICHSU-01 | Major P1 BE emit gap (verified 13:00 VV-QA-R9-BC-001 legacy) | **Downgrade Major P1 → Minor P3.** Seed VV1 YEU_CAU_BO_SUNG → BE emit entry ĐÚNG. Seed VV2 PHAN_CONG → canonical enum mới. R23 finding cũ là **legacy data**, không phải BE bug thực. Residual: FE thiếu i18n cho enum YEU_CAU_BO_SUNG → render raw string | Dev FE add label mapping i18n cho enum YEU_CAU_BO_SUNG (và 4 enum chưa map nếu cần) trong component Dòng thời gian |

**Kết luận seed walk:** 0 bug đóng mới, 1 bug downgrade severity (LICHSU Major→Minor), 2 bug giữ severity nhưng evidence chắc hơn (DG-013 + PC-WRN-01). Bug Major P1 list → 0; bug Open list → 3 (1×P2 Medium + 2×P3 Minor).

---

## 6. R25 reverify update (2026-05-16 10:30:00)

| # | Bug | R24 result | R25 fresh probe | Verdict |
|:-:|---|---|---|---|
| 1 | BUG-FUNC-DG-013 | Open Minor P3 (BE FIX ✓, FE generic /403) | Fresh `cb_nv_dp_02` STP-BG cross-cơ quan: API 3/3 endpoint trả `403 + ERR-DG-10 + "Bạn không có quyền xem kết quả đánh giá này"` ✓; FE `/403` render đúng spec text + "Mã lỗi: ERR-DG-10" — KHÔNG còn generic text | **CLOSED-VERIFIED** ✅ |
| 2 | BUG-VV-PC-WRN-01 | Open Minor P2 (no override) | Fresh `cb_nv_tw_01` VV-QA-R7-PRIVACY-DNAG002 (LV DN, DANG_KIEM_TRA) → modal Phân công → force `XXKHONGMATCH99` → `itemCount: 0`, `hasOverrideButton: false`, `dialogButtons: ["", "Hủy", "Xác nhận"]`. Empty message hint chỉ "Liên hệ QTHT / chọn vụ khác" | **OPEN unchanged** ❌ |
| 3 | BUG-VV-FN-LICHSU-01 | Open Minor P3 (FE fresh ✓, legacy hide UPDATE) | Fresh VV-BTP-TW-20260514-001 (YEU_CAU_BO_SUNG) → API `[YEU_CAU_BO_SUNG, TAO_VV]`, UI render "Yêu cầu bổ sung"/"Tạo vụ việc" ✓. Legacy VV-002 → API `[UPDATE, UPDATE, CREATE]`, UI vẫn render 1 "Tạo mới" | **OPEN unchanged** ⚠️ |

**Kết luận R25:** 1 bug đóng mới (DG-013 — FE fix surface đúng spec text + code), 2 bug giữ Open chờ dev fix. Bug Open list → 2 (1×P2 Medium + 1×P3 Minor).

---

## 7. R26 reverify update (2026-05-18 14:35:00)

| # | Bug | R25 result | R26 fresh probe | Verdict |
|:-:|---|---|---|---|
| 1 | BUG-VV-PC-WRN-01 | Open Minor P2 (no override) | Fresh `cb_nv_tw_01` VV-QA-R7-PRIVACY-DNAG002 (LV DN, DANG_KIEM_TRA) → modal Phân công → force `XXKHONGMATCH99` → `itemCount: 0`, `dialogButtons: ["", "Hủy", "Xác nhận"]`, `overrideHints: []`. Empty message hint chỉ "Liên hệ QTHT / chọn vụ khác" | **OPEN unchanged** ❌ |
| 2 | BUG-VV-FN-LICHSU-01 | Open Minor P3 (FE fresh ✓, legacy hide UPDATE) | Fresh VV-001 (`4a1a6889-...`) → API `[YEU_CAU_BO_SUNG, TAO_VV]`, UI "Yêu cầu bổ sung"/"Tạo vụ việc" ✓. Legacy VV-002 (`33b5a612-...`) → API vẫn `[UPDATE, UPDATE, CREATE]` (BE chưa migrate) NHƯNG UI render đủ 3 entries label tiếng Việt "Yêu cầu bổ sung"/"Kiểm tra"/"Tạo mới" — **FE FIX option (b) implemented** | **CLOSED-VERIFIED** ✅ |

**Kết luận R26:** 1 bug đóng mới (LICHSU-01 — FE fix option (b) derive label theo `duLieuMoi.trangThai`), 1 bug giữ Open chờ dev fix. Bug Open list → 1 (1×P2 Medium). File `Pass-bug-report-r7-7-3-functional-vu-viec.md` 100% Closed → rename `Pass-` prefix sau R26.

**Chi tiết R26:** [`r26-reverify-2026-05-18.md`](r26-reverify-2026-05-18.md) — 7 bảng + Tóm tắt cuối.
