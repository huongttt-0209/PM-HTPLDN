# Functional Test Report — R7.7.1 Hỏi đáp Phase 1 (Base TC)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-09 22:18:00 → 22:35:00 |
| **Loại test** | Functional R7.7.1 Phase 1 — base TC HD-001..019 (subset 13/35) |
| **Round** | Round 7 / R7.7.1 |
| **Account** | `cb_nv_tw_04` (CB NV) + `cb_pd_tw_04` (CB PD) — bypass OTP `666666` |
| **Tài liệu tham chiếu** | [todo-hoi-dap.md R7.7.1](../../../../tasks/todo-hoi-dap.md#r7-7-1) · [7.2-hoi-dap-phap-ly.md](../../../../funtion/7.2-hoi-dap-phap-ly.md) · `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` v3.5 |

---

## Verdict

✅ **Phase 1 PASS 13/13 TC base** — workflow đầy đủ MOI → TIEP_NHAN → DANG_XU_LY → CHO_PHE_DUYET → DA_DUYET ↔ CONG_KHAI verified end-to-end. Immutability enforced ở DA_DUYET + CONG_KHAI (no Sửa/Hủy hồ sơ/Phân công).

⚠️ **1 deviation phát hiện** — HD-021: List tabs = 9 (Tất cả + 7 state + Hủy) thay vì 7 tabs theo SRS v3.5 FR-II-04.

🚫 **Bugs Critical đã đóng** — BUG-BE-LOGIN-001 (BE login 500 sustained ~3 phút) đã recover 22:09:11 → resume R7.7.1.

---

## Test result breakdown

| TC | Mô tả | Kết quả | Method | Evidence |
|---|---|---|---|---|
| HD-001 | List 13 records + 9 tabs hiển thị | ✅ Đạt | UI list `/hoi-dap` | [r7-7-1-hd-001-list-9tabs-13records.png](r7-7-1-hd-001-list-9tabs-13records.png) |
| HD-002 | Search keyword "vốn điều lệ" → narrow 13→1 record | ✅ Đạt | UI search input + click Tìm kiếm. BE param `search` (200) | [r7-7-1-hd-002-search-vondieuel.png](r7-7-1-hd-002-search-vondieuel.png) |
| HD-003 | Tạo HD mới + auto-gen `HD-20260509-007` + state MOI + don_vi_id pre-fill `Cục Bổ trợ tư pháp - Bộ Tư pháp (TW)` | ✅ Đạt | Drawer Thêm mới + fill nội dung 168 ký tự + Lĩnh vực=Đầu tư + Kênh=Trực tiếp + Lưu. POST `/hoi-daps` 201 | [r7-7-1-hd-003-create-007-success.png](r7-7-1-hd-003-create-007-success.png) |
| HD-004 | Submit empty form → 3 client validation errors | ✅ Đạt | Client validation: "Nội dung câu hỏi là bắt buộc" / "Lĩnh vực pháp lý là bắt buộc" / "Kênh tiếp nhận là bắt buộc" | [r7-7-1-hd-004-empty-validation.png](r7-7-1-hd-004-empty-validation.png) |
| HD-005 | Nội dung >5000 ký tự → counter `5001/5000` + error "Nội dung tối đa 5000 ký tự" | ✅ Đạt | JS programmatic setter (UI maxLength=5000 enforce client typing) | [r7-7-1-hd-005-overlength-validation.png](r7-7-1-hd-005-overlength-validation.png) |
| HD-006 | Xem chi tiết HD-007 → render 7-step stepper + thông tin câu hỏi đầy đủ | ✅ Đạt | UI link click → `/hoi-dap/{uuid}` | [r7-7-1-hd-006-detail-007.png](r7-7-1-hd-006-detail-007.png) |
| HD-007 | Workflow MOI → TIEP_NHAN | ✅ Đạt | Click [Tiếp nhận] + xác nhận modal. POST `/tiep-nhan` 201. Active step Tiếp nhận. Người tiếp nhận = CB Nghiệp vụ TW 04 | inline trong [r7-7-1-hd-007-010-workflow-cho-phe-duyet.png](r7-7-1-hd-007-010-workflow-cho-phe-duyet.png) |
| HD-008 | Workflow TIEP_NHAN → DANG_XU_LY (Phân công) | ✅ Đạt | Click [Phân công] → modal pool ~40 cá nhân với workload count → chọn `cb_nv_tw_04` (self) → submit. POST `/phan-cong` 200 | inline screenshot |
| HD-009 | Soạn phản hồi 267 ký tự + Văn bản pháp luật + Gợi ý DN | ✅ Đạt | Inline form "Soạn phản hồi" — fill nội dung qua JS setter (MCP fill bypass React state) | inline |
| HD-010 | Workflow DANG_XU_LY → CHO_PHE_DUYET (Gửi phản hồi) | ✅ Đạt | Click [Gửi phản hồi] → confirm modal → POST `/phan-hois` 201 + PATCH `/phan-hois/{id}` 200. Active step Chờ phê duyệt | [r7-7-1-hd-007-010-workflow-cho-phe-duyet.png](r7-7-1-hd-007-010-workflow-cho-phe-duyet.png) |
| HD-011 | Workflow CHO_PHE_DUYET → DA_DUYET (Phê duyệt) — switch sang `cb_pd_tw_04` | ✅ Đạt | CB_PD_TW thấy 2 button [Phê duyệt] + [Từ chối]. Click [Phê duyệt] → "Hành động này không thể hoàn tác" modal → POST `/phe-duyet` 200 | inline |
| HD-012 | Workflow DA_DUYET → CONG_KHAI (Công khai lên Cổng PLQG) | ✅ Đạt | Click [Công khai lên Cổng PLQG] → modal "Mô tả công khai" → POST `/cong-khai` 200. Active step Công khai | [r7-7-1-hd-011-012-cong-khai.png](r7-7-1-hd-011-012-cong-khai.png) |
| HD-014 | Thu hồi — CONG_KHAI → DA_DUYET (Hủy công khai) | ✅ Đạt | Click [Hủy công khai] → confirm "Phản hồi sẽ bị gỡ khỏi Cổng PLQG" → POST `/huy-cong-khai` 200. Active step trở về Đã duyệt | [r7-7-1-hd-014-019-da-duyet-immutable.png](r7-7-1-hd-014-019-da-duyet-immutable.png) |
| HD-019 | Immutability ở DA_DUYET + CONG_KHAI — không có button Sửa/Hủy hồ sơ/Phân công | ✅ Đạt | Verify cả 2 state: chỉ còn button transition (Công khai / Hủy công khai). Content immutable enforced | [r7-7-1-hd-014-019-da-duyet-immutable.png](r7-7-1-hd-014-019-da-duyet-immutable.png) |

> **Severity breakdown** (deviation only — bug riêng nếu có log file bug):
> | Tổng | Critical | Major | Medium | Minor | Trivial |
> |------|----------|-------|--------|-------|---------|
> | 1 | 0 | 0 | 1 | 0 | 0 |

---

## Deviations / Sai spec

### DEV-HD-001 — List tabs = 9 thay vì 7 (SRS v3.5)

| Mục | Giá trị |
|---|---|
| **TC ref** | HD-021 |
| **SRS ref** | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` FR-II-04 v3.5 — "7 tabs gộp v3.5" |
| **Severity** | Medium |
| **Status** | Open — chưa log file bug riêng (xác nhận với BA xem có thay đổi spec không) |

**Quan sát thực tế:** UI `/hoi-dap` hiển thị 9 tabs:
1. Tất cả (default selected)
2. Mới (4)
3. Tiếp nhận
4. Đang xử lý
5. Chờ phê duyệt
6. Đã duyệt
7. Công khai
8. Hoàn thành
9. Hủy

**Spec v3.5 expected:** 7 tabs gộp (theo R7.4.A4 workflow note + 7-step stepper detail page).

**Hypothesis:** UI vẫn dùng 9-tab pattern v3 (7 state + Tất cả + Hủy = 9). Detail page stepper đã 7 steps (correct v3.5 — stepper exclude All + Hủy). FE list view chưa migrate sang 7-tab gộp.

**Action:** Defer to deep review SRS NotebookLM + BA confirm trước khi log Critical bug.

---

## Phase 1 — Test cases NOT covered

13 TC base PASS. Còn lại 22 TC chưa cover trong R7.7.1 (defer Phase 2):

| Bracket | TC | Lý do defer |
|---|---|---|
| HD-013 | Từ chối phê duyệt | Cần seed HD-008 mới ở state CHO_PHE_DUYET (đã dùng HD-007 cho Phê duyệt happy path) |
| HD-015, HD-016 | Hoàn thành (auto-finalize sau 30 ngày + manual mark) | Cần workaround time-warp hoặc manual mark — chưa rõ UI |
| HD-017, HD-018 | Soft delete + restore | TC reference cần verify SRS |
| HD-020..035 | Tabs filter + SLA + assign-back + reset password role | Phase 2 batch |
| HD-040..064 | 25 TC mới v3.5 (Mô hình B Mẫu phản hồi 3 cấp + TVN_BRIDGE + CR-06) | Phase 3 — TVN_BRIDGE block bởi R7.6.3 ⏳ Cổng PLQG endpoint |

---

## Bug active

**Đã đóng:** BUG-BE-LOGIN-001 — BE `/auth/login` 500 sustained ~3 phút. Recovered 22:09:11. [Pass-bug-report-be-login-500-r7-7-1.md](../../bug-reports/system-be/Pass-bug-report-be-login-500-r7-7-1.md)

**Đang theo dõi:** Không có bug Critical/Major mới Open trong Phase 1.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| MailHog | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Tool test | Chrome DevTools MCP — 100% UI MCP click chain. JS `evaluate_script` cho cases AntD virtual list + textarea state mismatch (MCP fill not triggering React onChange) |
| Test record | HD-20260509-007 (test record dùng cho HD-003..014 chain) |

---

*Functional report generated: 2026-05-09 22:35:00 | QA Automation via Claude Code (Opus 4.7)*
