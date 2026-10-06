# A4 — Edge Case Hunter Review (audit log)

> **Phase A step**: A4 (`bmad-review-edge-case-hunter`)
> **Ngày chạy**: 2026-05-10
> **Scope**: 7 file UC ct-htpldn-gd2/01..07
> **Iron rule**: TC mới merge inline vào file UC (Section "Edge bổ sung"). File này CHỈ là audit log (proposal + reasoning + merge mapping).

---

## 1. Edge case proposed (16 TC mới)

| # | TC ID đề xuất | File đích | Reasoning | Severity | Merge status |
|---|---------------|----------|-----------|----------|--------------|
| 1 | TC-LBC-012 | 01 | Idempotency double-click [Bắt đầu lập BC] — race condition khi user click nhanh 2 lần. Cần verify backend chỉ tạo 1 BC. | 🟡 P1 | ✅ Inline merged Section C |
| 2 | TC-LBC-013 | 01 | Guard CT TAM_DUNG → có cho phép lập BC trên đợt đã có không? SRS không nói rõ → log SPEC-CLARIFY. | 🟡 P1 | ✅ Inline merged Section C |
| 3 | TC-BC-013 | 02 | XSS sanitize nhan_xet — input text long từ user, browser render → bắt buộc test escape. BR-EC-13. | 🔴 P0 | ✅ Inline merged Section C |
| 4 | TC-BC-014 | 02 | Concurrent edit BC từ 2 tab — optimistic locking BR-EC-01. Critical vì BC có nhiều cell có thể race. | 🟡 P1 | ✅ Inline merged Section C |
| 5 | TC-BC-015 | 02 | Boundary số liệu lớn vượt int — cần verify backend dùng bigint/text, không silent overflow. | 🟡 P1 | ✅ Inline merged Section C |
| 6 | TC-BC-016 | 02 | Auto-save behavior — SRS không nói explicit, cần verify để cảnh báo user. | 🟢 P2 | ✅ Inline merged Section C |
| 7 | TC-TPD-013 | 03 | Idempotency Trình PD — race condition double-click → notification trùng cho CB PD. | 🟡 P1 | ✅ Inline merged Section C |
| 8 | TC-TPD-014 | 03 | Network failure rollback — verify atomicity 2 SM transition (đợt + BC). | 🟡 P1 | ✅ Inline merged Section C |
| 9 | TC-PD-BC-014 | 04 | XSS sanitize ly_do_tu_choi — render lại trong banner cho CB NV. BR-EC-13. | 🔴 P0 | ✅ Inline merged Section D |
| 10 | TC-PD-BC-015 | 04 | ly_do_tu_choi max length — SRS không define → SPEC-CLARIFY. | 🟢 P2 | ✅ Inline merged Section D |
| 11 | TC-PD-BC-016 | 04 | Audit dual entry verify — BR-DATA-05 yêu cầu audit cả 2 entity transition. | 🟡 P1 | ✅ Inline merged Section D |
| 12 | TC-GTW-013 | 05 | Network failure Gửi TW — verify rollback state. | 🟡 P1 | ✅ Inline merged Section C |
| 13 | TC-GTW-014 | 05 | BR-AUTH-08 scope notification — gửi tới CB NV TW nào. | 🟢 P2 | ✅ Inline merged Section C |
| 14 | TC-TH-015 | 06 | Tổng hợp 2 BC khác kỳ — block hay cho phép? SRS unclear → SPEC-CLARIFY. | 🟡 P1 | ✅ Inline merged Section C |
| 15 | TC-TH-016 | 06 | BC đã DA_TONG_HOP idempotency — không cho re-tổng hợp. | 🟡 P1 | ✅ Inline merged Section C |
| 16 | TC-TH-017 | 06 | Xuất file preview trước Lưu — UX behavior unclear. | 🟢 P2 | ✅ Inline merged Section C |
| 17 | TC-PERM-013 | 07 | DN/GV truy cập module — fill negative permission gap. | 🔴 P0 | ✅ Inline merged Section C |
| 18 | TC-PERM-014 | 07 | Session expired during action — BR-AUTH-01 boundary. | 🟡 P1 | ✅ Inline merged Section C |
| 19 | TC-PERM-015 | 07 | TK TAM_KHOA giữa session active — verify auth check on next request. | 🟢 P2 | ✅ Inline merged Section C |

> Note: Tổng 19 TC mới merge — đề xuất ban đầu 16 nhưng split thành 19 sau khi reasoning per-file (file 04 thêm 3 thay vì 2; file 07 thêm 3 thay vì 2).

## 2. Coverage delta sau A4

| File | Before A4 (A3 base) | A4 merged | After A4 |
|------|--------------------:|----------:|---------:|
| 01 - Bắt đầu lập BC | 5 | +2 | 7 |
| 02 - Lập BC | 8 | +4 | 12 |
| 03 - Trình PD BC | 6 | +2 | 8 |
| 04 - Phê duyệt BC | 9 | +3 | 12 |
| 05 - Gửi TW | 6 | +2 | 8 |
| 06 - Tổng hợp TW | 11 | +3 | 14 |
| 07 - Permission matrix | 6 | +3 | 9 |
| **TỔNG** | **51** | **+19** | **70** |

## 3. SPEC-CLARIFY mới phát sinh từ A4

| ID | TC liên quan | Tóm tắt |
|----|--------------|---------|
| SPEC-CLARIFY-CT-GD2-06 | TC-LBC-013 | Guard CT TAM_DUNG có cho phép lập BC không |
| SPEC-CLARIFY-CT-GD2-07 | TC-PD-BC-015 | ly_do_tu_choi max length |
| SPEC-CLARIFY-CT-GD2-08 | TC-TH-015 | Tổng hợp BC cross-kỳ block hay cho phép |

→ Cộng dồn với 5 SPEC-CLARIFY initial (00-test-plan-overview.md §6) = **8 SPEC-CLARIFY pending BA** sau A4.

## 4. Reasoning patterns áp dụng (BMAD edge-case-hunter heuristics)

- **Boundary cells**: số liệu vượt int (TC-BC-015), ký tự vượt limit (TC-BC-012, TC-PD-BC-015), batch size >100 (TC-TH-013).
- **Concurrency**: 2 tab edit (TC-BC-014), double-click trigger (TC-LBC-012, TC-TPD-013).
- **Failure injection**: Network 500 (TC-TPD-014, TC-GTW-013), session expired (TC-PERM-014).
- **State guard violations**: Đợt đã DA_TONG_HOP (TC-TH-016), CT TAM_DUNG (TC-LBC-013), BC ≠ trạng thái (TC-LBC-010, TC-TPD-011).
- **Security/sanitize**: XSS (TC-BC-013, TC-PD-BC-014), TK TAM_KHOA mid-session (TC-PERM-015).
- **Spec gaps**: Auto-save (TC-BC-016), preview xuất (TC-TH-017), cross-kỳ (TC-TH-015), CT TAM_DUNG (TC-LBC-013).

*Generated 2026-05-10 — Phase A step A4 (bmad-review-edge-case-hunter)*
