# Functional Test Report — R7.7.1 Hỏi đáp Phase 7 (Re-verify dev fix HD-021/022/016/053 + R7.6.3 probe)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-10 18:50:00 → 19:10:00 |
| **Loại test** | Re-verify 4 bug Open Phase 6 (HD-021/022/053/016) + probe R7.6.3 endpoint |
| **Round** | Round 7 / R7.7.1 Phase 7 |
| **Account** | `cb_pd_tw_04` (CB PD TW), `qtht_01` (QTHT) — bypass OTP `666666` |
| **Tool** | Chrome DevTools MCP — UI MCP click chain + `evaluate_script` API verify |

---

## Verdict

✅ **3/4 bug Closed-verified** + 🚫 **1/4 Open** + 🚫 **R7.6.3 chưa deploy → 13 TC defer vẫn block**

| BUG-ID | Severity | Verdict | Chi tiết |
|---|---|---|---|
| BUG-HD-021 | Minor | ✅ Closed-verified | Tab "Hoàn thành" trả 7/7 (3 HOAN_THANH + 4 HUY) — filter union `IN (HOAN_THANH, HUY)` đúng spec line 1033 |
| BUG-HD-022 | Minor | ✅ Closed-verified | 4/4 row SLA hiển thị "Sắp hết hạn 50–100% / Quá hạn > 100% (BR-SLA-02)", modal Ngưỡng 2 valuemax=100, value=100 |
| BUG-HD-016 | Minor | ✅ Closed-verified | GET `/api/v1/hoi-daps/{id}` sau Hủy CK trả `thoiGianDangTai=null` đúng BR-FLOW-09 line 1102 |
| BUG-HD-053 | Minor | 🚫 Vẫn Open | Modal CR-01 dialog `evaluate_script` chỉ có 2 button [Hủy/Công khai], không có text "Dùng ảnh mặc định" |

🚫 **R7.6.3 endpoint Cổng PLQG vẫn chưa deploy** — 7 candidate paths đều 404 (`/api/v1/cong-plqg/inbound/hoi-dap`, `/api/v1/cong-plqg/health`, `/api/v1/external/hoi-daps`, etc.) + filter `?kenhTiepNhan=TVN_BRIDGE` trả 0 records → 13 TC defer (HD-027/045/047/048/054/055/060/061/062 + HD-057 + HD-022b/c/d) vẫn block.

---

## Test result breakdown

| Bug | Method | Evidence |
|---|---|---|
| BUG-HD-021 | UI cb_pd_tw_04 → /hoi-dap → click tab "Hoàn thành" → `evaluate_script` count rows + read `totalText`. Result: `?tab=HOAN_THANH` trả `1-7 / 7 mục`, 7 rows gồm 3 HOAN_THANH + 4 HUY. | [r7-hd-021-retest-r10d-tab-hoanthanh-7records-union.png](../../bug-reports/hoi-dap/image/r7-hd-021-retest-r10d-tab-hoanthanh-7records-union.png) |
| BUG-HD-022 | UI qtht_01 → /quan-tri/cau-hinh tab "Thời hạn xử lý (SLA)" → snapshot 4 rows + click [Sửa] HOI_DAP → modal a11y inspect spinbutton "Ngưỡng cảnh báo 2 (%)" `value="100" valuemax="100" valuemin="1"`, button Increase disabled. | [r7-hd-022-retest-r10d-modal-nguong2-100-fixed.png](../../bug-reports/hoi-dap/image/r7-hd-022-retest-r10d-modal-nguong2-100-fixed.png) |
| BUG-HD-016 | UI cb_pd_tw_04 → HD-20260509-010 (DA_DUYET) → [Công khai] modal fill mô tả → submit → state CONG_KHAI thoiGianDangTai=2026-05-10T11:47:41.668Z. → [Hủy công khai] → confirm → state DA_DUYET. GET API: `congKhai=false, thoiGianDangTai=null`. | [r7-hd-016-retest-r10d-thoigian-null-fixed.png](../../bug-reports/hoi-dap/image/r7-hd-016-retest-r10d-thoigian-null-fixed.png) |
| BUG-HD-053 | UI cb_pd_tw_04 → HD-20260509-010 (DA_DUYET) → [Công khai] modal mở. `evaluate_script` inspect dialog: buttons=["", "Hủy", "Công khai"]; sections=[Mô tả công khai, Ảnh đại diện, Tệp đính kèm công khai]; hasDefaultImageText=false. | [r7-hd-053-retest-r10d-modal-still-missing-default-image-btn.png](../../bug-reports/hoi-dap/image/r7-hd-053-retest-r10d-modal-still-missing-default-image-btn.png) |
| R7.6.3 probe | `evaluate_script` fetch 7 candidate endpoints (`/api/v1/cong-plqg/inbound/hoi-dap`, `/cong-plqg/health`, `/cong-plqg/status`, `/cong-plqg/hoi-dap`, `/inbound/cong-plqg/hoi-dap`, `/external/hoi-daps`, `/cong-plqg/inbound`) + POST `/cong-plqg/inbound/hoi-dap` — tất cả trả 404 ERR-SYS-00-04-01. Filter TVN_BRIDGE: `?kenhTiepNhan=TVN_BRIDGE&size=5` → empty content. | — |

> **Severity breakdown defects mới (Phase 7):** 0 (chỉ re-verify, không log bug mới)

---

## Cumulative R7.7.1 sau Phase 7

| Phase | TC PASS | Tên |
|---|---|---|
| Phase 1 | 13 | HD-001..HD-014, HD-019 |
| Phase 2A | 4 | HD-013, HD-023, HD-024, HD-031 |
| Phase 2B | 7 | HD-029, HD-034, HD-035, HD-046, HD-056, HD-058, HD-063 |
| Phase 3a | 3 | HD-025, HD-026, HD-064 |
| Phase 3b | 2 | HD-030, HD-059 |
| Phase 4 | 7 | HD-020, HD-022 (partial), HD-028, HD-040, HD-041, HD-042, HD-043 (partial) |
| Phase 5 | 3 | HD-032, HD-044, HD-052 |
| Phase 6 | 3 | HD-015, HD-016 (caveat), HD-053 (caveat — upgrade Phase 7 caveat removed) |
| **Phase 7** | **0 TC mới** | **Re-verify pass HD-021/022/016 (đã đếm Phase 4-6) + Bug HD-053 vẫn Open + R7.6.3 vẫn block** |
| **Total** | **42** | **70% R7.7.1 coverage** |

🚫 **Defer còn lại 13 TC** (R7.6.3 + tooling — không thay đổi vs Phase 6):
- R7.6.3 Cổng PLQG endpoint: HD-027, HD-045, HD-047, HD-048, HD-054, HD-055, HD-060, HD-061, HD-062
- Backdated 30 ngày: HD-057
- Backend time-travel SLA: HD-022b/c/d (3 mức rendering)

---

## Bug active sau Phase 7

**Đã đóng Phase 7:** BUG-HD-021, BUG-HD-022, BUG-HD-016 (3 bug Closed-verified).

**Còn Open:** BUG-HD-053-DEFAULT-IMAGE-001 (Minor) — Modal CR-01 thiếu button "Dùng ảnh hệ thống mặc định".

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| API base | http://103.172.236.130:3000/api/v1 |
| Tool test | Chrome DevTools MCP — UI MCP click chain + `evaluate_script` cho DOM inspect + GET API verify state |
| Test record | HD-20260509-010 (DA_DUYET → CONG_KHAI → DA_DUYET full lifecycle để re-verify HD-016 + HD-053) |
| Multi-role isolation | isolatedContext `qtht_verify_r10d` (HD-022 SLA modal), default context `cb_pd_tw_04` (HD-021/053/016) |

---

*Functional report generated: 2026-05-10 19:10:00 | QA Automation via Claude Code (Opus 4.7)*
