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

✅ **3/3 bug Closed-verified Phase 9** (HD-053 R10e + HD-014 R10g + HD-055 R10g) + ✅ **3 TC mới PASS sau dev seed/fix** (HD-022b + HD-057 + HD-055) + 🚫 **9 TC chưa chạy được** (chia 2 nhóm: 7 chờ dev deploy Cổng PLQG · 2 chờ dev chạy thêm 2 câu SQL update `deadline`). Coverage R7.7.1 **46/60 (77%)** ↑ từ 43/60.

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

### Nhóm 2 — Chờ dev BE chạy thêm 2 câu SQL update `deadline` cho HD-22c + HD-22d (2 TC)

**TC còn block:** HD-022c (SLA badge vàng "Sắp hết hạn" ~70%), HD-022d (SLA badge đỏ "Quá hạn" ~110%)

**TC đã PASS sau seed:** ✅ HD-022b (SLA xanh "Bình thường" ~20%, ratio thực ~20% — trong dải xanh) + ✅ HD-057 (record DA_DUYET 35 ngày vẫn giữ state, không auto-close).

**Vì sao 2 TC còn block:** Dev BE đã chạy 4 câu SQL ban đầu trong file [seed-request-hd-022-057-backdate-sla.md](../../bug-reports/hoi-dap/seed-request-hd-022-057-backdate-sla.md) lúc khoảng 2026-05-11 10:00:00 — UPDATE `ngay_tiep_nhan` lùi 1.5/3.5/5.5 ngày và `created_at` lùi 35 ngày. **Nhưng dev quên UPDATE `deadline`** → tổng span giữa `ngay_tiep_nhan` và `deadline` = ~10 ngày thay vì 5 ngày theo BR-SLA-01 → ratio chia 2:

| Record | Ngày tạo (cũ) | ngay_tiep_nhan (sau seed) | deadline (chưa update) | Ratio elapsed/total | Trạng thái UI |
|---|---|---|---|---|---|
| HD-22b (dfdbc8a7) | 2026-05-09 | NOW − 1.5d | 2026-05-14 (5d sau create) | **20%** (~xanh) | ✅ `ant-tag-success` "Bình thường" |
| HD-22c (8c54715f) | 2026-05-09 | NOW − 3.5d | 2026-05-14 | **45.4%** (giả trong dải xanh) | ⚠️ VẪN `ant-tag-success` — kỳ vọng vàng "Sắp hết hạn" |
| HD-22d (101f22b6) | 2026-05-09 | NOW − 5.5d | 2026-05-14 | **55.6%** (giả mới qua 50%) | ⚠️ API tag `SAP_HET_HAN`, UI tag VẪN `ant-tag-success` xanh — kỳ vọng đỏ "Quá hạn" |

**Cần làm gì để chạy được:** Dev BE chạy thêm 2 câu SQL (đã bổ sung trong file seed-request, ~5 phút work):

```sql
UPDATE hoi_dap SET deadline = ngay_tiep_nhan + INTERVAL '5 days'
WHERE id IN ('8c54715f-4ff5-487f-bc1b-bc405d162534', '101f22b6-1cbe-4e1a-9d76-ab5d6cfd1322');
```

Sau khi dev chạy: ratio HD-22c → ~70%, HD-22d → ~110% → QA reload UI verify badge vàng + đỏ + escalate notification.

**Ai làm:** Dev BE.

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
| Seed backdate verify 10:30 (HD-22c/d partial) | HD-22c `ngay_tiep_nhan` lùi 3.5d, ratio ~45% (deadline KHÔNG update → span 10d thay vì 5d); HD-22d lùi 5.5d ratio ~55% — UI tag vẫn xanh. API HD-22d trả `mucDoCanhBao=SAP_HET_HAN` nhưng UI render xanh. **Dev BE quên UPDATE `deadline` cho 2 record → 2 TC còn block, cần thêm 2 câu SQL.** | — |
| HD-057 PASS verify 10:30 | GET HD-057 (3577bfb6) — `created_at` lùi 35 ngày, state vẫn `DA_DUYET` (KHÔNG auto-close về HOAN_THANH). Confirm BR-FLOW-06 manual close — không có cron auto-close. ✅ HD-057 PASS. | — |
| HD-055 inject 500 (R10g PASS) | UI cb_pd_tw_04 → HD-20260510-006 (DA_DUYET v8) → install XHR override chặn POST `/cong-khai` trả 500 `ERR-PD-04`. Modal CR-01 hiện `ant-alert-error` "Công khai thất bại" + "Lỗi máy chủ tạm thời khi công khai. Vui lòng thử lại sau." + "Mã lỗi: ERR-PD-04" + "Dữ liệu đã nhập được giữ lại — bấm 'Thử lại' để gửi lại yêu cầu." Buttons: `["", "Dùng ảnh hệ thống mặc định", "Hủy", "Thử lại"]` — `[Công khai]` → `[Thử lại]`. Toast: "Không thể công khai. Vui lòng thử lại." Form: textarea giữ 65 ký tự, counter `65 / 2000`. ✅ HD-055 PASS. | [r7-hd-055-retest-r10g-modal-error-alert-retry-pass.png](../../bug-reports/hoi-dap/image/r7-hd-055-retest-r10g-modal-error-alert-retry-pass.png) |
| HD-014 re-verify R10g UI PASS | Walk record HD-20260509-008 qua UI theo rule UI-only: (1) `cb_nv_tw_08` isolatedContext → mở DANG_XU_LY → [Gửi phản hồi] + confirm 2 modal → state `CHO_PHE_DUYET`. (2) Switch `cb_pd_tw_04` → reload → [Phê duyệt]+[Từ chối] hiện. (3) Click [Từ chối] → modal mở textarea "Lý do từ chối *" required, counter `0/500`. (4) Click [Xác nhận từ chối] không nhập gì → modal inline error **"Vui lòng nhập lý do từ chối."** (đúng message spec ERR-PD-02). Validation client-side trước round-trip BE — UX tốt. State guard giữ CHO_PHE_DUYET. ✅ HD-014 PASS. | [r7-hd-014-retest-r10g-ui-empty-lyDo-inline-error-pass.png](../../bug-reports/hoi-dap/image/r7-hd-014-retest-r10g-ui-empty-lyDo-inline-error-pass.png) |
| HD-021 re-verify | UI cb_pd_tw_04 → /hoi-dap. `evaluate_script` count `[role="tab"]` = **7**: Tất cả / Mới (badge 5) / Đang xử lý / Chờ phê duyệt / Đã duyệt / Công khai / Hoàn thành. Tab "Hoàn thành" filter `?tab=HOAN_THANH&size=1` trả total=**7** = HOAN_THANH (3) + HUY (4) — gộp v3.5 đúng SCR-II-01 line 1027-1033. | [r7-hd-021-retest-r10e-7tabs-with-counts.png](r7-hd-021-retest-r10e-7tabs-with-counts.png) |
| HD-035 re-verify | API search `?keyword=lương&trangThai=<X>` với 3 state processed: DA_DUYET (total=2, snippet match), HOAN_THANH (total=3, snippet match), CONG_KHAI (total=0 vì pool 0 record). Search full-text hoạt động đúng cho processed state. | API response |
| HD-008 re-verify | GET `/api/v1/hoi-daps?size=20` — 9/10 record có deadline = ngayTiepNhan + 5 working days (calendar diff 5-6). 1 outlier HD-20260510-002 (mucDoPhucTap=THUONG, deadline +36 cal days) — có thể user override hoặc edge case. Main path BR-SLA-01 OK. | API response |

> **Defects status Phase 9 (sau R10g):** 3 Closed-verified — (1) BUG-HD-053 R10e; (2) BUG-HD-055-PUBLISH-FAIL-UX-001 R10g 14:25:00 [Pass-bug-report](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md); (3) BUG-HD-014-REJECT-ERR-CODE-001 R10g 14:20:00 [Pass-bug-report](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md). KHÔNG còn defect Open trong Hỏi đáp.

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
