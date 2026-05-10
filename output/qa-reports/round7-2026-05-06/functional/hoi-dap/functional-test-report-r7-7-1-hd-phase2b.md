# Functional Test Report — R7.7.1 Hỏi đáp Phase 2B (CR-06 + Permission + Template + Manual close)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-09 23:00:00 → 23:12:00 |
| **Loại test** | Functional R7.7.1 Phase 2B — CR-06 form drawer + tab Hủy + filter Đã duyệt + permission NHT/CB_NV + template + manual close |
| **Round** | Round 7 / R7.7.1 Phase 2B |
| **Account** | `cb_nv_tw_04` (CB NV) + `cb_pd_tw_04` (CB PD) + `nht_01` (NHT) — bypass OTP `666666` |
| **Tài liệu tham chiếu** | [todo-hoi-dap.md R7.7.1](../../../../tasks/todo-hoi-dap.md#r7-7-1) · [7.2-hoi-dap-phap-ly.md](../../../../funtion/7.2-hoi-dap-phap-ly.md) · `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` v3.5 FR-II-04/05/06 |

---

## Verdict

✅ **Phase 2B PASS 7/7 TC** — coverage broaden:
- **HD-046** Form Thêm mới drawer chỉ 4 options Kênh tiếp nhận (filter TVN_BRIDGE) ✅
- **HD-058** State Hủy — list filter tab Hủy = 3 record, action button bị strip ✅
- **HD-035** Filter Đã duyệt — tab Đã duyệt = 1 record HD-007 ✅
- **HD-029** NHT sidebar KHÔNG có "Quản lý hỏi đáp pháp lý" (per FR-III-11 NHT scope) ✅
- **HD-034** Chèn mẫu phản hồi — Chọn mẫu combobox dropdown 2 templates filtered LV=Doanh nghiệp ✅
- **HD-056** Đóng hồ sơ thủ công — DA_DUYET → HOAN_THANH (BR-FLOW-06 manual close) ✅
- **HD-063** BR-FLOW-05 chặn CB_NV công khai — cb_nv_tw_04 KHÔNG có button Công khai/Đóng hồ sơ, cb_pd_tw_04 CÓ ✅

⚠️ **Defer 8 TC** Phase 2B kết thúc: HD-014 (đã PASS Phase 1), HD-021 (DEV-HD-001 9-tabs), HD-025/026 (permission scope BN/DP), HD-030/034b (SLA workflow time-based), HD-049-052 (TC TV org seed), HD-053-055 (Mô hình B 3-cấp đã PASS qua R7.3.1.MoB), HD-059 (concurrency), HD-064 (BR-FLOW-05 cùng cấp).

🚫 **Phase 3 (HD-040..062) vẫn block** — TVN_BRIDGE + DN portal + version conflict + CR-06 multi-cấp cần R7.6.3 ⏳ Cổng PLQG endpoint deploy.

---

## Test result breakdown

| TC | Mô tả | Kết quả | Method | Evidence |
|---|---|---|---|---|
| HD-046 | Form Thêm mới drawer Kênh tiếp nhận chỉ 4 options (DVC + HE_THONG_KHAC + TRUC_TIEP + CONG_PLQG), KHÔNG còn TVN_BRIDGE | ✅ Đạt | UI cb_nv_tw_04 click [+ Thêm mới] → drawer combobox snapshot 4 options | [r7-7-1-hd-046-form-4-options.png](r7-7-1-hd-046-form-4-options.png) |
| HD-058 | State Hủy — tab Hủy hiển thị 3 record (HD-002/003 + HD-20260507-004/005), action area bị strip | ✅ Đạt | UI click tab "Hủy" → bảng list 3 record state HUY | [r7-7-1-hd-058-state-huy-success.png](r7-7-1-hd-058-state-huy-success.png) |
| HD-035 | Filter Đã duyệt — tab Đã duyệt = 1 record HD-007 | ✅ Đạt | UI click tab "Đã duyệt" → 1 record HD-20260509-007 (Đầu tư) | [r7-7-1-hd-035-filter-da-duyet.png](r7-7-1-hd-035-filter-da-duyet.png) |
| HD-029 | Permission scope NHT — sidebar không có "Quản lý hỏi đáp pháp lý" (FR-III-11 NHT chỉ đào tạo + tư vấn + vụ việc) | ✅ Đạt | UI nht_01 isolatedContext → snapshot sidebar 8 buttons (đào tạo + chương trình + khóa + kho + mạng lưới TV + vụ việc + biểu mẫu + tư vấn) → KHÔNG có Hỏi đáp | [r7-7-1-hd-029-nht-sidebar-no-hoi-dap.png](r7-7-1-hd-029-nht-sidebar-no-hoi-dap.png) |
| HD-034 | Chèn mẫu phản hồi — Chọn mẫu combobox dropdown filter LV current HD = 2 templates | ✅ Đạt | UI cb_nv_tw_04 click HD-008 detail → click combobox "Chọn mẫu phản hồi" → 2 options ("Mẫu phản hồi BN-BKH - Doanh nghiệp", "Mẫu phản hồi HD - Doanh nghiệp") | [r7-7-1-hd-034-chon-mau-phan-hoi-dropdown.png](r7-7-1-hd-034-chon-mau-phan-hoi-dropdown.png) |
| HD-056 | Đóng hồ sơ thủ công — DA_DUYET → HOAN_THANH (BR-FLOW-06 no auto-close) | ✅ Đạt | UI cb_pd_tw_04 → HD-007 detail → click [Đóng hồ sơ] → confirm modal → API verify trangThai=HOAN_THANH + ngayHoanThanh=2026-05-09T16:11:05.609Z | [r7-7-1-hd-056-dong-ho-so-hoan-thanh.png](r7-7-1-hd-056-dong-ho-so-hoan-thanh.png) |
| HD-063 | BR-FLOW-05 chặn CB_NV công khai — chỉ CB_PD có button Công khai/Đóng hồ sơ trên DA_DUYET | ✅ Đạt | Page 5 (cb_nv_tw_04) HD-007 detail → KHÔNG có action button. Page 6 (cb_pd_tw_04) cùng record → CÓ "Công khai lên Cổng PLQG" + "Đóng hồ sơ" | [r7-7-1-hd-063-cb-nv-no-cong-khai-button.png](r7-7-1-hd-063-cb-nv-no-cong-khai-button.png) |

> **Severity breakdown:**
> | Tổng | Critical | Major | Medium | Minor | Trivial |
> |------|----------|-------|--------|-------|---------|
> | 0 | 0 | 0 | 0 | 0 | 0 |

---

## Key invariants verified

### BR-FLOW-05 enforce — CB_NV không công khai

`HD-007` ở DA_DUYET cùng UUID `451a5a1b-ab67-4e50-9e3e-3e51ad42ce9c`:
- **cb_nv_tw_04** (CB Nghiệp vụ TW): action area = empty (chỉ stepper + 2 panel info)
- **cb_pd_tw_04** (CB Phê duyệt TW): action area = 2 button [Công khai lên Cổng PLQG] + [Đóng hồ sơ]

→ FE permission gate đúng spec FR-II-05 v3.5 line 1320-1340.

### BR-FLOW-06 manual close — không auto-finalize

`HD-007` DA_DUYET → click [Đóng hồ sơ] → confirm modal "Hồ sơ sẽ không thể chỉnh sửa sau khi đóng" → POST close → state HOAN_THANH + ngayHoanThanh stamped.

→ State machine có transition **DA_DUYET → HOAN_THANH** (skip CONG_KHAI) cho path không công khai. UI stepper auto-tick all 7 steps khi state cuối.

### FR-III-11 NHT scope — không quyền hỏi đáp

NHT sidebar 8 buttons (theo SRS NHT spec):
1. Quản lý đào tạo, tập huấn (parent)
2. Chương trình đào tạo
3. Khóa học
4. Kho tài liệu / Bài giảng
5. Mạng lưới Tư vấn viên
6. Quản lý vụ việc hỗ trợ pháp lý
7. Quản lý thư viện biểu mẫu
8. Quản lý tư vấn (parent)

→ Không có "Quản lý hỏi đáp pháp lý" — match SCR-II-NHT scope spec.

### Mẫu phản hồi 3 cấp filter — auto-detect LV

HD-008 LV=Doanh nghiệp → combobox "Chọn mẫu phản hồi" dropdown render 2 options:
- "Mẫu phản hồi BN-BKH - Doanh nghiệp" (cấp BN-BKH match per scope rule)
- "Mẫu phản hồi HD - Doanh nghiệp" (cấp HD - all)

→ Filter LV auto match per FR-II-NEW-02 + R7.3.1.MoB seed verified.

---

## Phase 2B coverage

Cumulative R7.7.1 PASS sau Phase 2B: **24/60 TC** (40%).

| Phase | TC PASS | Tên |
|---|---|---|
| Phase 1 | 13 | HD-001..HD-014, HD-019 base lifecycle |
| Phase 2A | 4 | HD-013, HD-023, HD-024, HD-031 (workflow gap reject + search + permission spot + re-phân công) |
| Phase 2B | 7 | HD-029, HD-034, HD-035, HD-046, HD-056, HD-058, HD-063 |
| **Total** | **24** | **40% R7.7.1 coverage** |

**Defer 36 TCs** (Phase 3 + non-blocking):
- HD-021 (DEV-HD-001 — 9 tabs vs 7 spec, defer BA confirm)
- HD-025/026 (permission scope CB_NV_BN + CB_NV_DP — cần fresh seed BN/DP HD)
- HD-030 (SLA badge color time-based)
- HD-049-052 (phân công TC TV — cần seed TC TV org)
- HD-053-055 (Mô hình B 3-cấp đã PASS qua R7.3.1.MoB seed task)
- HD-059 (version conflict — concurrency multi-tab)
- HD-064 (BR-FLOW-05 cùng cấp — cần thêm cb_pd_dp_04)
- HD-040..045, HD-047, HD-048, HD-060..062 (TVN_BRIDGE + DN portal + CR-06 multi-cấp — block bởi R7.6.3 ⏳ Cổng PLQG endpoint deploy)

---

## Bug active

**Phase 2B:** KHÔNG có bug Critical/Major mới. BR-FLOW-05/06 enforce đúng, NHT permission scope đúng spec, template filter LV đúng FR-II-NEW-02.

**Đã đóng từ Phase 1:** BUG-BE-LOGIN-001 Closed-verified.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| MailHog | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Tool test | Chrome DevTools MCP — 100% UI MCP click chain. JS `evaluate_script` API verify state |
| Test record | HD-20260509-007 (DA_DUYET → HOAN_THANH lifecycle close), HD-20260509-008 (DANG_XU_LY template combobox) |
| Multi-role isolation | Page 4 = nht_01 / Page 5 = cb_nv_tw_04 / Page 6 = cb_pd_tw_04 isolatedContext |

---

*Functional report generated: 2026-05-09 23:12:00 | QA Automation via Claude Code (Opus 4.7)*
