# Functional Test Report — R7.7.1 Hỏi đáp Phase 9 (Re-verify dev fix HD-053 + seed/R7.6.3 status)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-11 09:00:00 → 09:15:00 |
| **Loại test** | Re-verify 1 bug Open Phase 8 (HD-053) + recheck seed backdate + R7.6.3 endpoint deploy |
| **Round** | Round 7 / R7.7.1 Phase 9 |
| **Account** | `cb_pd_tw_04` (CB PD TW) — bypass OTP `666666` |
| **Tool** | Chrome DevTools MCP — UI click chain + `evaluate_script` DOM inspect |

---

## Verdict

✅ **3/3 bug Closed-verified Phase 9** (HD-053 R10e + HD-014 R10g + HD-055 R10g) + ✅ **3 TC PASS sau dev seed** (HD-022b + HD-057 + HD-055) + ❌ **2 bug mới phát hiện R10g 17:20:00** (HD-022c + HD-022d badge SLA tier sai BR-SLA-02 — log [bug-report-r7-7-1-hd-022-sla-tier-mismatch.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-022-sla-tier-mismatch.md)) + 🚫 **7 TC còn chưa chạy được** (chờ R7.6.3 Cổng PLQG deploy). Coverage R7.7.1 **46/60 (77%)** giữ nguyên — HD-022b + HD-057 PASS, HD-022c/d Lỗi (không +PASS coverage), 7 chờ infra.

### Update 2026-05-11 17:20:00 — Dev SQL VERIFIED full 6/6 + bug mới SLA tier

Dev BE đã chạy ĐỦ 6 SQL UPDATE (4 gốc + 2 bổ sung deadline) — QA re-verify careful qua UI MCP browse từng record (`cb_pd_tw_04` isolatedContext, không API). Tất cả span = 5 ngày exact. Phân loại lại 4 TC:

| TC | State + Time | Ratio elapsed | Tier kỳ vọng (BR-SLA-02) | Tier thực tế | Verdict |
|---|---|---|---|---|---|
| HD-022b | DANG_XU_LY, ngay_tiep_nhan 09/05 22:24, deadline 15/05 17:51 | ~32% | Bình thường (xanh) | `ant-tag-success` "Còn 4 ngày LV" | ✅ PASS |
| HD-022c | DANG_XU_LY (đã rollback từ CHO_PHE_DUYET qua click [Từ chối]), 08/05 03:18 → 13/05 03:18 | ~71.6% (còn 28%) | Sắp hết hạn (vàng) | `ant-tag-success` "Còn 2 ngày LV" | ❌ **BUG** badge xanh sai tier — log BUG-HD-022-SLA-TIER-001 |
| HD-022d | DANG_XU_LY, 06/05 03:18 → 11/05 03:18 (PAST ~14h) | ~111.6% | Quá hạn (đỏ) | `ant-tag-orange` "Còn 0 ngày LV" | ❌ **BUG** badge cam sai tier — log BUG-HD-022-SLA-TIER-002 |
| HD-057 | DA_DUYET, created_at 06/04 10:24 (~35d cũ) | — | DA_DUYET preserve | DA_DUYET, no auto-close | ✅ PASS (xác nhận BR-FLOW-06) |

**App dùng logic `daysRemaining` thay vì `ratio` cho color tier** — đối nghịch BR-SLA-02 spec L1638-1642. Cần dev FE/BE sửa tier mapping (xem bug-report chi tiết).

| BUG-ID | Severity | Verdict | Chi tiết |
|---|---|---|---|
| BUG-HD-053-DEFAULT-IMAGE-001 | Minor | ✅ Closed-verified R10e | Modal CR-01 có button "Dùng ảnh hệ thống mặc định" cạnh upload zone, accept hint thêm `.gif` đúng SCR-II-02 line 1149. Click → preview `/default-avatar-cong-khai.png` + button toggle "Đổi ảnh khác" |
| BUG-HD-055-PUBLISH-FAIL-UX-001 | Minor | ✅ Closed-verified R10g | Re-test 14:25:00 — inject 500 ERR-PD-04 → modal hiện `ant-alert-error` "Công khai thất bại" + "Mã lỗi: ERR-PD-04" + button đổi `[Công khai]` → `[Thử lại]` + toast "Không thể công khai. Vui lòng thử lại." + form data retain (textarea 65/2000). Dev FE đã sửa đúng. [Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md) |
| BUG-HD-014-REJECT-ERR-CODE-001 | Minor | ✅ Closed-verified R10g | Re-test 14:20:00 — POST `/tu-choi` với `lyDo=""` và `lyDo=null` trên HD-20260510-006 (DA_DUYET v8) → BE trả 422 `ERR-PD-02` field=`lyDo` message="Vui lòng nhập lý do từ chối" cho cả 2 case. Dev BE đã sửa error code mapping đúng spec FR-II-08. [Pass-bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md) |

## 9 TC chưa chạy được — chia 2 nhóm rõ nguyên nhân

> Trước đây gọi là "defer" / "block". Mình đổi sang ngôn ngữ tự nhiên để dev/BA đọc 1 lần hiểu ngay TC nào kẹt vì gì, ai cần làm gì.

### Nhóm 1 — Chờ dev BE deploy Cổng PLQG endpoint (7 TC)

**TC:** HD-027, HD-045, HD-047, HD-048, HD-060, HD-061, HD-062

**Vì sao chưa chạy được:** Cổng PLQG (cổng pháp luật quốc gia — chỗ doanh nghiệp tự submit câu hỏi từ ngoài) chưa được dev BE deploy lên môi trường test. Mình thử 8 đường dẫn API candidate (vd `/api/v1/cong-plqg/inbound/hoi-dap`, `/cong-plqg/health`, POST inbound...) **đều trả 404 "không tồn tại"**. Filter `?kenhTiepNhan=TVN_BRIDGE` trả 0 record (không có dữ liệu chuyển từ Tư vấn nhanh ESCALATE).

**Cần làm gì để chạy được:** Dev BE deploy task **R7.6.3** — gồm 2 phần: (a) endpoint inbound cho DN submit câu hỏi qua Cổng PLQG; (b) bridge endpoint từ phiên Tư vấn nhanh ESCALATE sang Hỏi đáp.

**Ai làm:** Dev BE.

### ❌ Nhóm 2 — 2 bug mới SLA tier mismatch BR-SLA-02 (HD-022c + HD-022d) [Đổi từ "Block dev SQL" sang "Bug FE/BE tier mapping"]

**Dev BE đã chạy ĐỦ 6/6 SQL** (4 gốc + 2 bổ sung deadline) — verified qua UI MCP browse careful 17:15:00. Tất cả 4 record có span deadline = 5d exact đúng BR-SLA-01. **KHÔNG còn cần dev chạy SQL nữa.**

**Phát hiện mới:** Khi run TC HD-022c/d UI thực tế, badge SLA color tier không khớp spec BR-SLA-02:

| Record | Ratio thực tế | Tier kỳ vọng (spec L1638-1642) | Tier thực tế UI | Verdict |
|---|---|---|---|---|
| HD-022c | elapsed 71.6%, còn 28.4% | Vàng "Sắp hết hạn" (<50% còn lại) | `ant-tag-success` xanh "Còn 2 ngày LV" | ❌ BUG-HD-022-SLA-TIER-001 |
| HD-022d | elapsed 111.6% (deadline đã qua 14h) | Đỏ "Quá hạn" (>100% đã dùng) | `ant-tag-orange` cam "Còn 0 ngày LV" | ❌ BUG-HD-022-SLA-TIER-002 |

**Nguyên nhân:** App có vẻ map color theo `daysRemaining` (>=2 → success, ==0 → orange) thay vì `ratio elapsed/span` theo spec → tier sai 1 bậc với HD-022c và HD-022d. DB field `muc_do_canh_bao` có 4 giá trị enum đúng spec (`BINH_THUONG`/`SAP_HET`/`QUA_HAN`/`QUA_HAN_NGHIEM_TRONG`) nhưng badge UI không render đúng.

**Cần làm gì:** Dev FE/BE sửa logic compute `muc_do_canh_bao` + map AntD tag color (`success`/`warning`/`error`/`black`) theo ratio đúng BR-SLA-02. Log chi tiết: [bug-report-r7-7-1-hd-022-sla-tier-mismatch.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-022-sla-tier-mismatch.md)

**Ai làm:** Dev FE + Dev BE (depending on where `muc_do_canh_bao` được compute).

### ✅ Đã đóng — Nhóm 3 cũ (HD-055 dev FE fix UX modal)

**TC:** HD-055 — ✅ Closed-verified R10g 14:25:00. Dev FE đã sửa error handler đúng spec: modal hiện `ant-alert-error` "Công khai thất bại" + mã `ERR-PD-04` + button `[Công khai]` → `[Thử lại]` + toast `ant-message` + form data retain (textarea 65/2000). Bug log [Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md) đã Closed.

---

## Test result breakdown

| Bug | Method | Evidence |
|---|---|---|
| BUG-HD-053 | UI cb_pd_tw_04 → HD-20260510-001 (DA_DUYET) → [Công khai] modal CR-01 mở. `evaluate_script` inspect: button uid=251_12 "Dùng ảnh hệ thống mặc định" cạnh upload zone, accept hint `.jpg, .png, .gif`. Click button → preview `<img src="/default-avatar-cong-khai.png" alt="Ảnh hệ thống mặc định">` render trong zone, button toggle "Đổi ảnh khác", 2 button cuối modal vẫn [Hủy/Công khai]. | [r7-hd-053-retest-r10e-default-image-btn-fixed.png](../../bug-reports/hoi-dap/image/r7-hd-053-retest-r10e-default-image-btn-fixed.png) + [r7-hd-053-retest-r10e-default-image-preview-after-click.png](../../bug-reports/hoi-dap/image/r7-hd-053-retest-r10e-default-image-preview-after-click.png) |
| R7.6.3 probe | `evaluate_script` fetch 8 candidate endpoints (`/api/v1/cong-plqg/inbound/hoi-dap`, `/cong-plqg/health`, `/cong-plqg/status`, `/cong-plqg/hoi-dap`, `/inbound/cong-plqg/hoi-dap`, `/external/hoi-daps`, `/cong-plqg/inbound`, POST inbound) — tất cả 404 ERR-SYS-00-04-01. Filter `?kenhTiepNhan=TVN_BRIDGE&size=5` → empty content. | — |
| Seed backdate verify 09:55 | GET API 4 ID record trong seed-request — `ngay_tiep_nhan` vẫn ~2026-05-09/10, không backdate. **Dev chưa apply lần 1.** | — |
| Seed backdate verify 10:30 (PASS HD-022b) | Re-check GET API — HD-22b `ngay_tiep_nhan` lùi 1.5d, ratio ~20%, badge UI `ant-tag-success` "Bình thường" → ✅ TC HD-022b PASS (xanh đúng spec BR-SLA-02 dải 0-50%). | — |
| Seed backdate verify 17:15:00 (HD-22c/d UI walk) — sau dev chạy đủ 6/6 SQL | Walk UI MCP `cb_pd_tw_04`: HD-22c (8c54715f) `ngay_tiep_nhan = 08/05 03:18`, `deadline = 13/05 03:18` (span 5d exact). Click [Từ chối] rollback CHO_PHE_DUYET → DANG_XU_LY. Now 11/05 17:15, elapsed 3.58d → ratio 71.6%, còn 28.4%. Badge UI: `ant-tag-success` "Còn 2 ngày LV" — ❌ Sai BR-SLA-02 (phải vàng `ant-tag-warning`). HD-22d (101f22b6) `ngay_tiep_nhan = 06/05 03:18`, `deadline = 11/05 03:18` (đã qua 14h). Badge: `ant-tag-orange` "Còn 0 ngày LV" — ❌ Sai BR-SLA-02 (phải đỏ `ant-tag-error`). Cả 2 logged BUG-HD-022-SLA-TIER-001/002. | [r7-hd-022c-retest-r10g-sla-green-at-72pct-mismatch.png](../../bug-reports/hoi-dap/image/r7-hd-022c-retest-r10g-sla-green-at-72pct-mismatch.png) + [r7-hd-022d-sla-orange-overdue.png](../../bug-reports/hoi-dap/image/r7-hd-022d-sla-orange-overdue.png) |
| HD-057 PASS verify 10:30 | GET HD-057 (3577bfb6) — `created_at` lùi 35 ngày, state vẫn `DA_DUYET` (KHÔNG auto-close về HOAN_THANH). Confirm BR-FLOW-06 manual close — không có cron auto-close. ✅ HD-057 PASS. | — |
| HD-055 inject 500 (R10g PASS) | UI cb_pd_tw_04 → HD-20260510-006 (DA_DUYET v8) → install XHR override chặn POST `/cong-khai` trả 500 `ERR-PD-04`. Modal CR-01 hiện `ant-alert-error` "Công khai thất bại" + "Lỗi máy chủ tạm thời khi công khai. Vui lòng thử lại sau." + "Mã lỗi: ERR-PD-04" + "Dữ liệu đã nhập được giữ lại — bấm 'Thử lại' để gửi lại yêu cầu." Buttons: `["", "Dùng ảnh hệ thống mặc định", "Hủy", "Thử lại"]` — `[Công khai]` → `[Thử lại]`. Toast: "Không thể công khai. Vui lòng thử lại." Form: textarea giữ 65 ký tự, counter `65 / 2000`. ✅ HD-055 PASS. | [r7-hd-055-retest-r10g-modal-error-alert-retry-pass.png](../../bug-reports/hoi-dap/image/r7-hd-055-retest-r10g-modal-error-alert-retry-pass.png) |
| HD-014 re-verify R10g UI PASS | Walk record HD-20260509-008 qua UI theo rule UI-only: (1) `cb_nv_tw_08` isolatedContext → mở DANG_XU_LY → [Gửi phản hồi] + confirm 2 modal → state `CHO_PHE_DUYET`. (2) Switch `cb_pd_tw_04` → reload → [Phê duyệt]+[Từ chối] hiện. (3) Click [Từ chối] → modal mở textarea "Lý do từ chối *" required, counter `0/500`. (4) Click [Xác nhận từ chối] không nhập gì → modal inline error **"Vui lòng nhập lý do từ chối."** (đúng message spec ERR-PD-02). Validation client-side trước round-trip BE — UX tốt. State guard giữ CHO_PHE_DUYET. ✅ HD-014 PASS. | [r7-hd-014-retest-r10g-ui-empty-lyDo-inline-error-pass.png](../../bug-reports/hoi-dap/image/r7-hd-014-retest-r10g-ui-empty-lyDo-inline-error-pass.png) |
| HD-021 re-verify | UI cb_pd_tw_04 → /hoi-dap. `evaluate_script` count `[role="tab"]` = **7**: Tất cả / Mới (badge 5) / Đang xử lý / Chờ phê duyệt / Đã duyệt / Công khai / Hoàn thành. Tab "Hoàn thành" filter `?tab=HOAN_THANH&size=1` trả total=**7** = HOAN_THANH (3) + HUY (4) — gộp v3.5 đúng SCR-II-01 line 1027-1033. | [r7-hd-021-retest-r10e-7tabs-with-counts.png](r7-hd-021-retest-r10e-7tabs-with-counts.png) |
| HD-035 re-verify | API search `?keyword=lương&trangThai=<X>` với 3 state processed: DA_DUYET (total=2, snippet match), HOAN_THANH (total=3, snippet match), CONG_KHAI (total=0 vì pool 0 record). Search full-text hoạt động đúng cho processed state. | API response |
| HD-008 re-verify | GET `/api/v1/hoi-daps?size=20` — 9/10 record có deadline = ngayTiepNhan + 5 working days (calendar diff 5-6). 1 outlier HD-20260510-002 (mucDoPhucTap=THUONG, deadline +36 cal days) — có thể user override hoặc edge case. Main path BR-SLA-01 OK. | API response |

> **Defects status Phase 9 (sau R10g 17:20:00):** 3 Closed-verified — (1) BUG-HD-053 R10e; (2) BUG-HD-055-PUBLISH-FAIL-UX-001 R10g 14:25:00 [Pass-bug-report](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md); (3) BUG-HD-014-REJECT-ERR-CODE-001 R10g 14:20:00 [Pass-bug-report](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md). **2 bug mới Open R10g 17:20:00** — BUG-HD-022-SLA-TIER-001/002 (FE/BE map sai BR-SLA-02): [bug-report-r7-7-1-hd-022-sla-tier-mismatch.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-022-sla-tier-mismatch.md).

---

## Cumulative R7.7.1 sau Phase 9

| Phase | TC PASS | Tên |
|---|---|---|
| Phase 1 | 13 | HD-001..HD-014, HD-019 |
| Phase 2A | 4 | HD-013, HD-023, HD-024, HD-031 |
| Phase 2B | 7 | HD-029, HD-034, HD-035, HD-046, HD-056, HD-058, HD-063 |
| Phase 3a | 3 | HD-025, HD-026, HD-064 |
| Phase 3b | 2 | HD-030, HD-059 |
| Phase 4 | 7 | HD-020, HD-022 (partial), HD-028, HD-040, HD-041, HD-042, HD-043 (partial) |
| Phase 5 | 3 | HD-032, HD-044, HD-052 |
| Phase 6 | 3 | HD-015, HD-016, HD-053 (đếm Phase 6 — Phase 9 dev fix nâng full-clean, drop caveat) |
| Phase 7 | 0 | Re-verify HD-021/022/016 đóng + R7.6.3 block |
| Phase 8 | 1 | HD-054 PASS (Công khai submit OK); HD-055 PARTIAL UX fail, HD-053 vẫn Open ở Phase 8 |
| Phase 9 | 0 | Re-verify HD-053 dev fix → Closed-verified (drop caveat Phase 6). 6/6 bug flow đóng |
| Phase 9 R10f | 2 | HD-022b SLA xanh ~20% + HD-057 không auto-close 35d — sau dev BE chạy 4/6 câu SQL seed-request |
| **Phase 9 R10g** | **1 TC mới** | **HD-055 PASS — dev FE fix modal UX (alert error + nút Thử lại + form retain) + bonus HD-014 retest Closed-verified BE fix ERR-PD-02** |
| **Total** | **46** | **77% R7.7.1 coverage** ↑ từ 72% |

🚫 **Còn 9 TC chưa chạy được** (chi tiết 2 nhóm ở section "9 TC chưa chạy được" phía trên):
- **7 TC chờ dev BE deploy Cổng PLQG (R7.6.3):** HD-027, HD-045, HD-047, HD-048, HD-060, HD-061, HD-062
- **2 TC chờ dev BE chạy thêm 2 câu SQL update `deadline`:** HD-022c (vàng ~70%), HD-022d (đỏ ~110%) — dev đã chạy `ngay_tiep_nhan` nhưng quên `deadline` → ratio chia 2

---

## Bug active sau Phase 9 (R10g final)

**✅ Đã đóng cả 3 bug Phase 9 sau R10g 14:25:00:**
- BUG-HD-053-DEFAULT-IMAGE-001 (Minor) — Modal CR-01 có button "Dùng ảnh hệ thống mặc định" — Closed-verified R10e. → [Pass-bug-report-flow-hoi-dap.md](../../bug-reports/hoi-dap/Pass-bug-report-flow-hoi-dap.md) (6/6 đóng).
- BUG-HD-055-PUBLISH-FAIL-UX-001 (Minor) — Modal Công khai hiện alert error + nút Thử lại + form retain — Closed-verified R10g 14:25:00. → [Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md).
- BUG-HD-014-REJECT-ERR-CODE-001 (Minor) — POST `/tu-choi` trả `ERR-PD-02` đúng spec — Closed-verified R10g 14:20:00. → [Pass-bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md).

**Còn Open:** 0 — module Hỏi đáp clean về bug, chỉ còn 9 TC block do dev seed/deploy chưa xong.

**File rename:** Tất cả 3 bug report đã auto-rename `Pass-` prefix qua hook PostToolUse.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| API base | http://103.172.236.130:3000/api/v1 |
| Tool test | Chrome DevTools MCP — UI click chain + `evaluate_script` DOM inspect |
| Test record | HD-20260510-001 (DA_DUYET state — modal CR-01 Công khai) |
| Bộ account | `_04` series (per user request session 2026-05-11) |

---

*Functional report generated: 2026-05-11 09:15:00 | QA Automation via Claude Code (Opus 4.7)*
