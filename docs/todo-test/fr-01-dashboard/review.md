# Review — FR-01 Dashboard test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:35:00

## Gaps

- **G1 — KPI-03 v3 vs v3.5 enum không cite line v3 chứng minh delta.** Plan note §7 item 3 nói "v3 đếm 3 state (`DA_TIEP_NHAN`, `DANG_XU_LY`, `DA_PHAN_CONG`)" nhưng `srs-v3/srs-fr-01-dashboard.md:423` thực tế chỉ liệt kê 3 state với drill-down `?trang_thai=DANG_XU_LY` (single state). Plan suy luận tập 3 state nhưng SRS v3 không quote rõ — cần cite cụ thể v3 line nào, hoặc đánh dấu là "interpret" để BA chốt. TC-03.x đang test 5 state có nguy cơ tester confuse khi data từ FR-05 chỉ ở 3 state.

- **G2 — Filter Q1 (`Năm bắt đầu sử dụng phần mềm`) chưa có TC test rỗng DB.** §7 Q1 raise đúng ambiguity (`srs-update-2026-5-5/srs-fr-01-dashboard.md:180`) nhưng không có TC tương ứng trong §4 (vd "DB rỗng → dropdown Năm hiển thị gì?"). Đây là edge case P0 — env reset hoặc UAT đầu tiên sẽ trigger ngay.

- **G3 — Cross-module integration TC mới có 6, plan claim ≥5/6 PASS criteria — không cover KPI-05/06 với FR-03.** TC-05/06 (KPI-05/06 ↔ FR-03 KHOA_HOC) thiếu trong §4 cross-module list dù KPI-05 `DANG_DIEN_RA` và KPI-06 `DA_KET_THUC` đều cần seed từ FR-03. Hệ quả: nếu FR-03 chưa sẵn sàng, TC-05.1/06.1 không có dependency record → 🚫 không phân loại đúng nguyên nhân nhóm E.

- **G4 — Permission scope chip phạm vi cho QTHT chưa phân biệt v3.5 update.** Plan §2.3 cột "Chip phạm vi mặc định" cho QTHT = "Tất cả địa phương" nhưng SRS v3.5 không quote nguyên văn label này cho QTHT (chỉ inferred từ row CB_NV_TW). Cần grep `srs-update-2026-5-5/...:682-686` hoặc §SCR-I-01 cho QTHT chip text — hiện đang chế text → false negative khi tester so exact match.

- **G5 — Auto-refresh `tab hidden` (Page Visibility) thiếu TC cụ thể.** §1.1 nói "Page Visibility API" nhưng §4 TC-12 (auto-refresh 7 TC) không break-down riêng cho hidden-tab pause. SRS line `srs-update-2026-5-5/srs-fr-01-dashboard.md:114-122` flow F4 nêu rõ "Tab active?" → No → pause. Cần ít nhất 1 TC test `document.hidden=true` (qua devtools throttle hoặc minimize tab).

- **G6 — Sample nhỏ N<10 chỉ test ở UC8/UC9 (TC-08, TC-09).** SRS line 487 quote rule áp dụng cho cả UC8 trái + phải + UC9. Plan có TC-09.1 mention donut "N học viên" nhưng chưa có TC riêng cho biểu đồ UC8 phải (SLA) khi N<10 — đảm bảo dấu `*` + tooltip generic "(< 10 vụ việc)". Edge này dễ miss khi seed pool nhỏ.

- **G7 — Drill-down URL persist filter — không test legacy URL `?tu_ngay=...&den_ngay=...`.** §7 item 1 raise đúng "test legacy URL → auto-default" nhưng §4 TC-13/14 không có TC negative cho deprecated params (`srs-update-2026-5-5/...:768`). Đây là regression sau migrate v3 → v3.5, browser bookmark cũ sẽ vẫn dùng URL legacy.

- **G8 — Trạng thái 30 banner ≥50% widget × 3 chu kỳ — chưa có TC orchestration thực tế.** TC-12 cap 7 nhưng test "3 chu kỳ liên tiếp ≥50% widget fail" cần network throttle + mock 6/12 widget timeout 30s × 3 lần = ~3 phút setup. Plan không break-down step seed/mock cho TC này — risk skip vì khó tái hiện.

- **G9 — BR-TREND chéo năm (Tháng=1 → Y-1 tháng 12) chỉ map vào TC-01.3/03.4.** SRS `srs-update-2026-5-5/...:195` quote rule chéo năm + "Nhật ký lịch sử không đủ → '—'". TC plan chưa nêu cụ thể test data cần seed Y-1 tháng 12 cho KPI-01 — chưa có hệ thống audit log Y-1 thì TC-01.3 sẽ assert "—" mọi lúc → false pass.

- **G10 — Không có TC explicit cho v3.5 BR-AUTH-04 chốt "ngang cấp" (BN không thấy ĐP).** TC-15.4 ghi "TW aggregate" nhưng negative case BN/ĐP cross-check (BN login → KHÔNG thấy ĐP data) cần ít nhất 1 TC riêng test BN switch L1=DP → expect locked. Hiện chỉ có TC-15 cho "BN scope BN của user".

## Suggestions

- **S1 — Tách §4 cross-module list thành bảng riêng với cột "Upstream task ID gốc"** (vd TC-04.1 cần task FR-05 R{N}.X seed HOAN_THANH). Khi block, tester dễ trace dependency theo Rule 2 trong CLAUDE.md (`[need: ≥N entity state X]`).

- **S2 — Bổ sung 2 TC cho KPI-05/06 ↔ FR-03 KHOA_HOC** vào cross-module list (đạt 8 TC integration thay vì 6). Pattern: seed 4 KHOA_HOC `DANG_DIEN_RA` ở ĐP-AG + 3 `DA_KET_THUC` với `ngay_ket_thuc` trong kỳ filter → assert KPI-05=4, KPI-06=3.

- **S3 — Trong §1.3 thêm cột "Negative permission expected" cho DN/TVV/CG/NHT** — ghi rõ redirect URL expected (`/cong-doanh-nghiep` cho DN, `/vu-viec/cua-toi` cho TVV) thay vì chỉ "Redirect Nhóm IV/V" chung chung. Khi tester assert URL sẽ có exact target.

- **S4 — Đổi format cite SRS line từ `srs-update-2026-5-5/srs-fr-01-dashboard.md:740-768` (range) sang line cụ thể duy nhất** (vd `:740` cho "năm bắt đầu sử dụng" + `:768` riêng cho "URL legacy auto-default"). Range cite khó verify khi BA push back.

- **S5 — Bổ sung mục "Test data prerequisite checklist" trước §4** liệt kê 9 entity upstream × state cần có. Format: `□ ≥1 HOI_DAP state=MOI ĐP-AG (FR-02 task X)` × 9 dòng. Tester onboard mới biết ngay seed nào miss.

- **S6 — §5 exit criteria nêu "cross-module integration ≥5/6 PASS" — nâng lên "≥7/8 PASS"** sau khi thêm 2 TC KPI-05/06. Đồng thời thêm gate: "ZERO TC permission scope FAIL" (đã có ở §5 nhưng chỉ cho 15.x — extend qua P0 toàn bộ §4).

- **S7 — Thêm subsection "Risk register" cuối §7** liệt kê risk env (vd BE chưa expose endpoint trend chéo năm, mock server timeout 30s cần infra confirm). Risk register là input cho Bảng 2 "Cần làm gì để chạy" khi viết test report.

- **S8 — Note §7 13 delta — đánh dấu rõ delta nào đã có TC cover, delta nào defer.** Vd "Δ1 filter → TC-13.x (covered)", "Δ8 auto-refresh per-widget → TC-12.x (covered)", "Δ13 N<10 chú giải mẫu nhỏ → TC-09.1 (UC9 only, UC8 chưa cover — xem G6)". Giúp BA review nhanh coverage gap.

## Verdict

**REVISE** — Plan có cấu trúc tốt (15 file TC, 60 TC tổng, phân bổ priority hợp lý, 13 delta v3.5 list rõ, BR mapping đầy đủ). Tuy nhiên cần fix trước khi sign-off:

1. **G1 + G9** (state enum + trend chéo năm) là critical correctness gap — risk false pass khi test data không khớp logic SRS.
2. **G3 + G10 + S2** (cross-module + permission negative) cần đạt ≥7 integration TC thay vì 6 để cover đủ 7 KPI có drill-down.
3. **G7** (legacy URL) và **G5** (Page Visibility) là 2 edge case bắt buộc cho regression v3 → v3.5.
4. **S5** (prerequisite checklist) + **S1** (cross-module dependency table) cần thêm để execution dễ trace block nhóm A/E.

Sau khi address 10 gap + bổ sung 8 suggestion (chủ yếu G1, G3, G5, G7, G9, S2, S5, S8) — plan đủ chất lượng để BA sign-off và tester viết TC detail. Hiện trạng plan đã match SRS v3.5 ~85% (delta 13 list đủ, BR 14 mapping đủ, permission 11 role đủ) — chỉ cần fix correctness gap + tăng coverage cross-module + thêm edge case là sẵn sàng.
