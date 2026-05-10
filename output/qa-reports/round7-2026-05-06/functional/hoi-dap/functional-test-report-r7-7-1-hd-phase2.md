# Functional Test Report — R7.7.1 Hỏi đáp Phase 2 (Workflow gap + Permission spot)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-09 22:44:00 → 23:05:00 |
| **Loại test** | Functional R7.7.1 Phase 2 — workflow gap (HD-013 từ chối + HD-031 re-phân công) + filter (HD-023) + permission spot (HD-024) |
| **Round** | Round 7 / R7.7.1 |
| **Account** | `cb_nv_tw_04` (CB NV) + `cb_pd_tw_04` (CB PD) — bypass OTP `666666` |
| **Tài liệu tham chiếu** | [todo-hoi-dap.md R7.7.1](../../../../tasks/todo-hoi-dap.md#r7-7-1) · [7.2-hoi-dap-phap-ly.md](../../../../funtion/7.2-hoi-dap-phap-ly.md) · `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` v3.5 |

---

## Verdict

✅ **Phase 2A PASS 4/4 TC** — workflow gap closed:
- **HD-013** Từ chối phê duyệt (cả negative validation + happy path transition) ✅
- **HD-023** Search by mã HD code ✅
- **HD-031** Re-phân công on DANG_XU_LY (nguoiPhanCongId mutate, state preserved) ✅
- **HD-024** Permission CB_NV_TW không thấy Phê duyệt/Từ chối button trên CHO_PHE_DUYET ✅ (implicit từ Phase 1 + cross-check Phase 2)

⚠️ **Phase 2B defer 21 TCs** còn lại (HD-014 hủy công khai đã PASS Phase 1, HD-021 9-tabs đã DEV-HD-001, HD-029 soft delete + HD-025/026 permission + HD-049-052 phân công TC TV + HD-030/034/035/046/053-058/063/064 chưa cover).

🚫 **Phase 3 (HD-040..064) vẫn block** — TVN_BRIDGE + DN portal + version conflict cần R7.6.3 ⏳ Cổng PLQG endpoint deploy.

---

## Test result breakdown

| TC | Mô tả | Kết quả | Method | Evidence |
|---|---|---|---|---|
| HD-013a | Từ chối phê duyệt — submit lý do trống → BR-FLOW-04 enforce error "Vui lòng nhập lý do từ chối." | ✅ Đạt | UI MCP click Từ chối → submit empty → modal stays open + textarea aria-invalid=true + error message visible | [r7-7-1-hd-013-tu-choi-empty-validation.png](r7-7-1-hd-013-tu-choi-empty-validation.png) |
| HD-013b | Từ chối phê duyệt — fill 221 ký tự lý do → POST `/tu-choi` 200 → state CHO_PHE_DUYET → DANG_XU_LY + lyDoTuChoi stored + ngayDuyet=null | ✅ Đạt | UI cb_pd_tw_04 click Từ chối → JS setter fill reason → click Xác nhận từ chối → API verify state | [r7-7-1-hd-013-cho-phe-duyet-pd-buttons.png](r7-7-1-hd-013-cho-phe-duyet-pd-buttons.png) · [r7-7-1-hd-013-tu-choi-success-back-dangxuly.png](r7-7-1-hd-013-tu-choi-success-back-dangxuly.png) |
| HD-023 | Search by mã HD code "HD-20260509-008" → narrow 15→1 record | ✅ Đạt | UI fill keyword field + click Tìm kiếm → BE param `search` → 1 record returned | [r7-7-1-hd-023-search-ma-hd.png](r7-7-1-hd-023-search-ma-hd.png) |
| HD-024 | CB Nghiệp vụ TW không thấy button Phê duyệt/Từ chối khi HD ở CHO_PHE_DUYET | ✅ Đạt | Page 1 (cb_nv_tw_04) sau Gửi phản hồi → state CHO_PHE_DUYET nhưng action area chỉ còn Phân công + Cập nhật thời hạn + Sửa. Page 3 (cb_pd_tw_04) cùng record → có Phê duyệt + Từ chối | inline trong [r7-7-1-hd-013-cho-phe-duyet-pd-buttons.png](r7-7-1-hd-013-cho-phe-duyet-pd-buttons.png) |
| HD-031 | Re-phân công on DANG_XU_LY (post-từ chối) — pool reload, workload count update, mutate nguoiPhanCongId mà không đổi state | ✅ Đạt | UI click Phân công → modal open trên DANG_XU_LY → pick cb_nv_tw_02 (workload=1) → Phân công → API verify state=DANG_XU_LY + nguoiPhanCongId=facdea31 | [r7-7-1-hd-031-rephancong-on-dangxuly.png](r7-7-1-hd-031-rephancong-on-dangxuly.png) · [r7-7-1-hd-031-rephancong-success.png](r7-7-1-hd-031-rephancong-success.png) |

> **Severity breakdown:**
> | Tổng | Critical | Major | Medium | Minor | Trivial |
> |------|----------|-------|--------|-------|---------|
> | 0 | 0 | 0 | 0 | 0 | 0 |

---

## Workflow gap closed — HD-A (HD-20260509-008) lifecycle

Test record `HD-20260509-008` (UUID `8c54715f-4ff5-487f-bc1b-bc405d162534`) đi qua full reject path:

```
MOI (22:44:00, cb_nv_tw_04 tạo)
  ↓ Tiếp nhận
TIEP_NHAN (22:45:00, cb_nv_tw_04)
  ↓ Phân công self
DANG_XU_LY (22:45:30, cb_nv_tw_04)
  ↓ Soạn phản hồi 477 ký tự + Gửi
CHO_PHE_DUYET (22:46:00, cb_nv_tw_04)
  ↓ cb_pd_tw_04 Từ chối "[R7.7.1 HD-013] Phản hồi chưa đầy đủ..."
DANG_XU_LY (22:48:00, lyDoTuChoi stored, ngayDuyet=null)
  ↓ cb_nv_tw_04 Re-phân công sang cb_nv_tw_02
DANG_XU_LY (23:00:00, nguoiPhanCongId=facdea31, state preserved)
```

Verified key invariants:
- **BR-FLOW-04 enforce client validation** — required reason on Từ chối (regex check 0/500 + aria-invalid=true)
- **State machine reverse transition** — CHO_PHE_DUYET → DANG_XU_LY hợp lệ (không phải full reset về MOI)
- **Field persistence** — lyDoTuChoi giữ trong DB sau reject + hiển thị block "Lý do từ chối" ở detail page
- **Re-phân công on DANG_XU_LY** — không tạo state transition mới, chỉ mutate nguoiPhanCongId
- **Permission segregation** — CB_NV_TW không có button phê duyệt/từ chối trên CHO_PHE_DUYET (chỉ CB_PD_TW)

---

## Phase 2A — Test cases NOT covered (defer Phase 2B)

| Bracket | TC | Lý do defer |
|---|---|---|
| HD-014 | Hủy công khai (CONG_KHAI → DA_DUYET) | Đã PASS Phase 1 (HD-007) — không cần re-test |
| HD-015, HD-016 | Hoàn thành (auto-finalize 30 ngày + manual) | Cần workaround time-warp hoặc manual mark |
| HD-021 | Tabs filter | Đã DEV-HD-001 Phase 1 — UI 9 tabs vs SRS 7 tabs |
| HD-025, HD-026 | Permission CB_NV_DP / CB_NV_BN | Cần switch role + verify scope filter |
| HD-029 | Soft delete (MOI / TIEP_NHAN) | Cần tạo HD MOI mới riêng để delete + verify isDeleted=true |
| HD-030, HD-034, HD-035 | SLA / deadline / cập nhật thời hạn | Cần workflow + time-based verification |
| HD-046, HD-049-052 | Phân công Tổ chức tư vấn (TC org branch) | Cần seed TC TV organization data + role permission verify |
| HD-053-058 | Mô hình B Mẫu phản hồi 3 cấp + auto-fill | Phase 3 — cần FR-II-NEW-02 fully integrated |
| HD-063, HD-064 | CR-06 don_vi_id pre-fill verify multi-cấp | Phase 3 — cần switch role TW/BN/DP để cross-check |
| HD-040..064 | TVN_BRIDGE + DN portal + version conflict | Phase 3 — block bởi R7.6.3 ⏳ Cổng PLQG endpoint |

Tổng coverage R7.7.1 sau Phase 2A: **17/60 TC PASS** (28%).

---

## Bug active

**Đã đóng:** BUG-BE-LOGIN-001 (Phase 1) đã Closed-verified.

**Phase 2A:** KHÔNG có bug Critical/Major mới. BR-FLOW-04 enforce đúng, state machine + permission segregation đúng spec v3.5.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| MailHog | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Tool test | Chrome DevTools MCP — 100% UI MCP click chain. JS `evaluate_script` fill textarea (MCP fill not triggering React onChange) |
| Test record | HD-20260509-008 (UUID `8c54715f-4ff5-487f-bc1b-bc405d162534`) — single HD recycle qua reject path để cover HD-013 + HD-031 |
| Multi-role isolation | Page 1 = cb_nv_tw_04 default context. Page 3 = cb_pd_tw_04 isolatedContext — switch role không cần logout |

---

*Functional report generated: 2026-05-09 23:05:00 | QA Automation via Claude Code (Opus 4.7)*
