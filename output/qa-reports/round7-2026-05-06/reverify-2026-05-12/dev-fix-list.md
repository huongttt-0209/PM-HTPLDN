# Danh sách bug cần dev fix — Sau R23-verify3 seed walk 2026-05-14 13:45:00 (UI-first + fresh seed)

**Tổng cộng: 3 bug Open** (R23-reverify đóng thêm 1: BUG-E2E-S4-011 đã FIX — FE đổi sang gọi `loaiDanhMuc=LOAI_HINH_HO_TRO`, dropdown render 6 options). **R23-verify3 13:45:00** — verify lại 3 bug bằng UI-first + **fresh seed VV LV Đất đai** (per user feedback "seed dữ liệu để test"): seed 2 VV mới qua form Nhập thủ công UI walk → walk state machine YEU_CAU_BO_SUNG (VV1) + Đạt → DA_PHAN_CONG (VV2) → test modal Phân công với meaningful keyword. Bug 1 (DG-013) — Minor P3 wording residual `ERR-AUTH-VPD-00-02` cross-cơ quan thay vì spec `ERR-DG-10`; verify đã thực hiện R23-verify3 12:30:00 trước seed walk, kết quả không đổi. Bug 2 (VV-PC-WRN-01) — **fresh seed VV2 LV Đất đai** state DANG_KIEM_TRA → modal Phân công DOM probe: 6 control (radio Cá nhân/Tổ chức + dropdown gợi ý + textarea ghi chú) + 2 button [Hủy]/[Xác nhận], **KHÔNG có override mechanism**; gõ keyword `hương tvv1` (TVV-BTP-TW-0029 HOAT_DONG, LV "Dân sự/Hành chính/Lao động/Thuế" — KHÔNG Đất đai, verified qua `/api/v1/tu-van-viens` global) → listbox empty với message **"Trống — Không tìm thấy đối tượng phù hợp lĩnh vực — Liên hệ QTHT để mở rộng lĩnh vực TVV/NHT, hoặc chọn vụ khác"** → BE LV-locked enforced, FE hint user 2 path (contact QTHT / đổi vụ), KHÔNG có "tìm thủ công" per `srs-fr-05-vu-viec.md:781`. Bug structural confirmed real với fresh data + active TVV pool. Bug 3 (VV-FN-LICHSU-01) — **fresh seed VV1 LV Đất đai** Kết luận "Yêu cầu bổ sung" → state YEU_CAU_BO_SUNG; API `/lich-su` trả `[YEU_CAU_BO_SUNG, TAO_VV]` 2 entries — **BE EMIT entry đúng ✓** (R23 finding cũ "BE silent" RESOLVED). Tuy nhiên timeline UI render raw enum `YEU_CAU_BO_SUNG` thay vì label "Yêu cầu bổ sung" — FE thiếu label mapping. **Fresh seed VV2** Phân công → API `/lich-su` `[PHAN_CONG, KIEM_TRA, TAO_VV]` canonical enum mới (không còn legacy `CREATE/UPDATE/APPROVE/PHAN_CONG_CA_NHAN`); UI render đúng label "Phân công"/"Kiểm tra"/"Tạo vụ việc". **Bug 3 downgrade Major P1 → Minor P3**: residual chỉ là FE label i18n mapping cho 1 enum (YEU_CAU_BO_SUNG), không phải BE emit gap.

| Phân loại | Số lượng |
|---|:-:|
| P0 Critical | 0 |
| P1 Major | 0 |
| P2 Medium | 1 (BUG-VV-PC-WRN-01 — modal override mechanism, dev FE+BE) |
| P3 Minor | 2 (BUG-FUNC-DG-013 wording mismatch · BUG-VV-FN-LICHSU-01 FE label mapping i18n) |

---

## 1. Bảng 3 bug Open cần dev fix

| # | Bug ID | Module | Sev | P | Ai làm | Tóm tắt fix | File bug report |
|:-:|---|---|:-:|:-:|:-:|---|---|
| 1 | BUG-FUNC-DG-013 | Đánh giá HQ | Minor | P3 | Dev BE + FE | **R23 deep-verify — VPD gate đã FIX** ✓ (CB NV match cơ quan xem được KQ HOAN_THANH). **Wording mismatch ở 2 lớp**: (a) BE code 403 cross-cơ quan trả `ERR-AUTH-VPD-00-02`, spec `srs-fr-08-danh-gia.md:786` yêu cầu `ERR-DG-10`; (b) UI: FE auto-redirect `/403` page render text generic "Bạn không có quyền truy cập trang này" thay vì spec text "Bạn không có quyền xem kết quả đánh giá này". Dev: đổi mapping BE + thêm domain-specific 403 page cho Đánh giá HQ. | [bug-report-r22-fr-vi-10.md](../bug-reports/danh-gia/bug-report-r22-fr-vi-10.md) |
| 2 | BUG-VV-PC-WRN-01 | Vụ việc | Minor | P2 | Dev FE + BE | **R23-verify3 fresh seed — confirmed real với active TVV pool.** Seed VV2 LV Đất đai → state DANG_KIEM_TRA → modal Phân công DOM probe: 6 control (radio Cá nhân/Tổ chức + dropdown gợi ý + textarea ghi chú) + 2 button [Hủy]/[Xác nhận], không có override mechanism. Gõ keyword `hương tvv1` (TVV-BTP-TW-0029 HOAT_DONG, LV ngoài Đất đai, verified API global) → listbox empty với message **"Trống — Không tìm thấy đối tượng phù hợp lĩnh vực — Liên hệ QTHT để mở rộng lĩnh vực TVV/NHT, hoặc chọn vụ khác"**. BE LV-locked enforced, FE hint 2 path (QTHT / đổi vụ), KHÔNG có "tìm thủ công" per `srs-fr-05-vu-viec.md:781`. Dev FE+BE bổ sung mechanism (button/toggle/clear-LV/dropdown unfiltered). | [bug-report-flow-vu-viec.md](../bug-reports/vu-viec/bug-report-flow-vu-viec.md) |
| 3 | BUG-VV-FN-LICHSU-01 | Vụ việc | Minor | P3 | Dev FE | **R23-verify3 fresh seed — BE emit gap RESOLVED ✓, residual FE label i18n.** Seed VV1 LV Đất đai → Kết luận "Yêu cầu bổ sung" → API `/lich-su` trả `[YEU_CAU_BO_SUNG, TAO_VV]` — BE emit entry ĐÚNG. Seed VV2 → Phân công → API `[PHAN_CONG, KIEM_TRA, TAO_VV]` canonical enum (không còn legacy `CREATE/UPDATE/APPROVE/PHAN_CONG_CA_NHAN`). Tuy nhiên timeline UI render raw enum `YEU_CAU_BO_SUNG` thay vì label "Yêu cầu bổ sung" — FE thiếu i18n mapping. Dev FE bổ sung label cho enum YEU_CAU_BO_SUNG (và 4 enum còn lại nếu chưa map) trong component Dòng thời gian. **Downgrade Major P1 → Minor P3** (data layer OK, chỉ presentation gap). | [bug-report-r7-7-3-functional-vu-viec.md](../bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md) |

---

## 2. Bug đã Closed R20+R22+R22-verify2+R23-reverify (10 bug)

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
| ~~BUG-E2E-S4-011~~ | Cross-cutting | **R23-reverify 2026-05-14 01:05** — Fresh probe MCP DN `9999999990`: modal "Gửi yêu cầu hỗ trợ pháp lý" → dropdown "Loại hình hỗ trợ" render 6 options đúng spec (Tư vấn pháp luật / Tham gia tố tụng / Đại diện ngoài tố tụng / Hòa giải / Đào tạo/bồi dưỡng / Trợ giúp khác). Network: FE gọi `GET /api/v1/danh-muc/tree?loaiDanhMuc=LOAI_HINH_HO_TRO` → 200 (reqid=211), KHÔNG còn gọi `LOAI_HINH_HT`. FE đã align với FR-10 source-of-truth. R22-verify trước verify sai method — probe API direct 2 key thay vì capture FE request thực tế. |

**File đã rename `Pass-` prefix:** TVCS-R16 / HDTV-7-14 / E2E-seam-gaps / E2E-S4-loai-hinh-empty.

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
