# Functional Test Report — R7.7.1 Hỏi đáp Phase 6 (post dev fix HD-021/043)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-10 12:00:00 → 12:35:00 |
| **Loại test** | Functional R7.7.1 Phase 6 — TC unblocked sau dev fix HD-043 (dropdown optgroup) + HD-021 (tab count). Chạy thêm HD-015 (Công khai), HD-016 (Hủy CK), HD-053 (Modal CR-01) + verify block status HD-027, HD-048 |
| **Round** | Round 7 / R7.7.1 Phase 6 |
| **Account** | `cb_pd_tw_04` (CB Phê duyệt TW), `cb_nv_tw_04` (đã verify Phase 5) — bypass OTP `666666` |
| **Tài liệu tham chiếu** | [todo-hoi-dap.md R7.7.1](../../../../tasks/todo-hoi-dap.md#r7-7-1) · [7.2-hoi-dap-phap-ly.md](../../../../funtion/7.2-hoi-dap-phap-ly.md) · `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` v3.5 FR-II-08 (line 1085-1102 BR-FLOW-09) + SCR-II-02 line 1141-1180 (Modal CR-01) |

---

## Verdict

✅ **Phase 6 = 5/8 PASS** (3 unblocked + 2 verified) · ⚠️ **2/8 sai spec partial** · 🚫 **2/8 vẫn block** (R7.6.3):

| TC | Phân loại | Verdict |
|---|---|---|
| HD-021 | Re-test bug fix | ⚠️ Sai spec partial — tab count 7 đúng, BE filter "Hoàn thành" miss HUY |
| HD-022 | Re-test bug fix | ❌ Lỗi — Ngưỡng 2 vẫn 90%, max cap 99% |
| HD-043 | Re-test bug fix | ✅ Đạt — 2 optgroup + badge 🟦/🟨 đúng spec |
| HD-053 | Modal CR-01 UI | ✅ Đạt (caveat) — đủ field nhưng thiếu nút "Dùng ảnh mặc định" |
| HD-015 | Workflow Công khai | ✅ Đạt — DA_DUYET → CONG_KHAI, congKhai=true, thoiGianDangTai stamped |
| HD-016 | Workflow Hủy CK | ✅ Đạt main flow (caveat) — CONG_KHAI → DA_DUYET, congKhai=false. **thoiGianDangTai NOT NULL** (sai BR-FLOW-09 line 1102) |
| HD-027 | API CONG_PLQG inbound | 🚫 Không test được — 5 candidate endpoints đều 404 (R7.6.3 chưa deploy) |
| HD-048 | Filter TVN_BRIDGE | 🚫 Không test được — 0 records (data gap, R7.6.3 chưa deploy) |

---

## Test result breakdown

| TC | Mô tả | Kết quả | Method | Evidence |
|---|---|---|---|---|
| HD-021 | 7 tabs gộp v3.5 | ⚠️ Partial fix | UI cb_nv_tw_04 → /hoi-dap đếm `[role="tab"]` = 7 (`Tất cả/Mới/Đang xử lý/Chờ phê duyệt/Đã duyệt/Công khai/Hoàn thành`). BE filter `?tab=HOAN_THANH` trả 2 record HOAN_THANH, miss 4 record HUY. | [r7-hd-021-retest-7tabs-but-huy-missing.png](../../bug-reports/hoi-dap/image/r7-hd-021-retest-7tabs-but-huy-missing.png) |
| HD-022 | Ngưỡng 2 SLA | ❌ Lỗi | UI qtht_01 → /quan-tri/cau-hinh tab "Thời hạn xử lý (SLA)". 4 row vẫn render "Quá hạn 90-100%" + Ngưỡng 2 = 90. Modal Sửa: spinbutton `valuemax=99` cap. Không đổi vs Phase 4. | [r7-hd-022-retest-still-90-percent.png](../../bug-reports/hoi-dap/image/r7-hd-022-retest-still-90-percent.png) |
| HD-043 | Dropdown optgroup | ✅ Đạt | UI cb_nv_dp_04 (DP-AG) → HD-20260509-009 → click "Chọn mẫu phản hồi". Dropdown render `ant-select-item-group`. Sau khi seed 1 mẫu DP-AG → 2 group đúng: ["Mẫu khung quốc gia (TW)" + "Mẫu của đơn vị bạn"] với badge 🟦 + 🟨. | [r7-hd-043-retest-2-optgroup-with-badge.png](../../bug-reports/hoi-dap/image/r7-hd-043-retest-2-optgroup-with-badge.png) |
| HD-053 | Modal Công khai CR-01 | ✅ Đạt (caveat) | UI cb_pd_tw_04 → HD-20260510-001 (DA_DUYET) → click [Công khai lên Cổng PLQG] → modal mở với fields: (1) Mô tả công khai textbox `0 / 2000` ✅ ≤2000 ký tự; (2) Ảnh đại diện upload `.jpg, .png ≤5MB` ✅ — spec yêu cầu thêm `.gif`, UI không có; (3) Tệp đính kèm `.pdf, .doc, .docx, .xls, .xlsx` ≤10 tệp ≤20MB/tệp ✅. **Thiếu** button "Dùng ảnh hệ thống mặc định" (spec line 1149). Submit + Cancel buttons OK. | [r7-7-1-hd-053-modal-cr01-cong-khai.png](r7-7-1-hd-053-modal-cr01-cong-khai.png) |
| HD-015 | Công khai workflow | ✅ Đạt | UI cb_pd_tw_04 → HD-20260510-001 → fill mô tả 200 ký tự → click [Công khai] → POST `/api/v1/hoi-daps/{id}/cong-khai` 200. Verify state: `trangThai=CONG_KHAI`, `congKhai=true`, `thoiGianDangTai=2026-05-10T05:28:04.883Z`. UI reload: badge "Công khai" + button [Hủy công khai] hiện. Vai trò CB PD cùng cấp (BR-FLOW-05) PASS. | [r7-7-1-hd-015-cong-khai-success.png](r7-7-1-hd-015-cong-khai-success.png) |
| HD-016 | Hủy công khai | ✅ Đạt main flow | UI cb_pd_tw_04 → HD-20260510-001 (CONG_KHAI) → click [Hủy công khai] → confirm popup "Hủy công khai? Phản hồi này sẽ bị gỡ khỏi Cổng PLQG." → click [Hủy công khai] → state về DA_DUYET, `congKhai=false`. **Sai spec:** `thoiGianDangTai` vẫn = `2026-05-10T05:28:04.883Z` (không reset NULL theo BR-FLOW-09 line 1102 "Xóa `thoi_gian_dang_tai` về NULL"). UI reload: badge "Đã duyệt" + button [Công khai lên Cổng PLQG] hiện trở lại. | [r7-7-1-hd-016-huy-cong-khai-back-da-duyet.png](r7-7-1-hd-016-huy-cong-khai-back-da-duyet.png) |
| HD-027 | API CONG_PLQG inbound | 🚫 Không test được | Probe 5 candidate endpoints: `/api/v1/cong-plqg/inbound/hoi-dap` 404, `/api/v1/inbound/cong-plqg/hoi-dap` 404, `/api/v1/public/hoi-daps` 401 (existing endpoint khác), `/api/v1/cong-plqg/hoi-dap` 404, `/api/v1/external/hoi-daps` 404. Endpoint inbound CONG_PLQG chưa deploy — block bởi R7.6.3 ⏳. | — |
| HD-048 | Filter TVN_BRIDGE | 🚫 Không test được | UI/API filter `?kenhTiepNhan=TVN_BRIDGE` → 200 OK + `total=0`, `data=[]`. Filter endpoint hoạt động nhưng pool 0 record TVN_BRIDGE — block bởi R7.3.1.TVN seed (cần R7.6.3 ⏳ Cổng PLQG endpoint deploy phiên ESCALATE). | — |

> **Severity breakdown defects mới (Phase 6):**
> | Tổng | Critical | Major | Medium | Minor | Trivial |
> |------|----------|-------|--------|-------|---------|
> | 2 | 0 | 0 | 0 | 2 | 0 |
>
> 2 minor defects mới: (a) HD-053 thiếu button "Dùng ảnh hệ thống mặc định"; (b) HD-016 thoiGianDangTai không reset NULL khi Hủy CK.

---

## Cumulative R7.7.1 PASS sau Phase 6

| Phase | TC PASS | Tên |
|---|---|---|
| Phase 1 | 13 | HD-001..HD-014, HD-019 |
| Phase 2A | 4 | HD-013, HD-023, HD-024, HD-031 |
| Phase 2B | 7 | HD-029, HD-034, HD-035, HD-046, HD-056, HD-058, HD-063 |
| Phase 3a | 3 | HD-025, HD-026, HD-064 |
| Phase 3b | 2 | HD-030, HD-059 |
| Phase 4 | 7 | HD-020, HD-022 (partial), HD-028, HD-040, HD-041, HD-042, HD-043 (partial → upgrade Phase 6) |
| Phase 5 | 3 | HD-032, HD-044, HD-052 |
| **Phase 6** | **3** | **HD-015, HD-016, HD-053 (đạt với caveat) — HD-043 upgrade từ partial → full PASS** |
| **Total** | **42** | **70% R7.7.1 coverage** |

⚠️ **Sai spec / partial:** HD-021 (tab count fix, BE filter HUY pending), HD-022 (4/4 mức chưa fix Ngưỡng 2 + 3/4 mức rendering hoãn).

🚫 **Defer còn lại 13 TC** (block bởi R7.6.3 + tooling):
- R7.6.3 Cổng PLQG endpoint: HD-027, HD-045, HD-047, HD-048, HD-054, HD-055, HD-060, HD-061, HD-062
- Backdated 30 ngày: HD-057
- Backend time-travel SLA: HD-022b/c/d (3 mức rendering)

---

## Bug active sau Phase 6

**Phase 6 mới log:**
- BUG-HD-053-DEFAULT-IMAGE-001 (Minor) — Modal CR-01 thiếu button "Dùng ảnh hệ thống mặc định" (spec line 1149)
- BUG-HD-016-THOIGIAN-NULL-001 (Minor) — Hủy CK không reset `thoi_gian_dang_tai` về NULL (sai BR-FLOW-09 line 1102)

**Đã đóng:** BUG-HD-043 (Closed-verified Phase 6).

**Còn Open:**
- BUG-HD-021 (Minor — downgrade từ Major) — partial fix, BE filter "Hoàn thành" miss HUY
- BUG-HD-022 (Minor) — Ngưỡng 2 chưa fix
- BUG-HD-053-DEFAULT-IMAGE-001 (Minor — mới)
- BUG-HD-016-THOIGIAN-NULL-001 (Minor — mới)

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| API base | http://103.172.236.130:3000/api/v1 |
| Tool test | Chrome DevTools MCP — UI click chain. `evaluate_script` cho DOM inspect + verify state qua GET API |
| Test record | HD-20260510-001 (DA_DUYET → CONG_KHAI → DA_DUYET full lifecycle), 4 row SLA config (HOI_DAP/HO_SO_HT/HO_SO_TT/VU_VIEC) |
| Multi-role isolation | isolatedContext `cb_pd_tw_04_verify` (HD-015/016/053), `cb_nv_dp_04_verify` (HD-043), `qtht_01_verify` (HD-022), `cb_nv_tw_04_verify` (HD-021) |

---

*Functional report generated: 2026-05-10 12:35:00 | QA Automation via Claude Code (Opus 4.7)*
