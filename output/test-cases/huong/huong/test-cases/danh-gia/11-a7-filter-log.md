# A7 — Manual UI/Function-Testable Filter Log (FR-08 Đánh giá HQ)

> **Ngày chạy:** 2026-05-10
> **Mode:** Manual review
> **Rule:** Loại / sửa TC chỉ test được DB/API thuần — Edit IN-PLACE file UC tương ứng
> **Total TC trước A7:** 144 → **sau A7:** 144 (0 LOẠI / 1 SỬA / 0 NEW)

---

## Phân loại quyết định

| Decision | Count | Note |
|----------|-------|------|
| GIỮ (UI/function-testable trực tiếp qua MCP chrome-devtools / qa-only) | 143 | Đa số TC kiểm tra được qua UI flow, toast, badge, table, filter, modal |
| SỬA (rephrase để bớt phụ thuộc DB/API thuần) | 1 | TC-DG-PC-023 — DELETE PHAN_CONG: thêm verify "row biến mất khỏi bảng" thay vì verify DB AUDIT_LOG thuần |
| LOẠI (chỉ test DB/API thuần, không UI) | 0 | — |

---

## TC SỬA inline

### TC-DG-PC-023 — Refined verification (UI-testable)

**Trước (A6 fill):**
> Expected: Row biến mất. AUDIT_LOG có DELETE. Số người PC giảm 1

**Sau A7 (đã edit IN-PLACE file 03):**
- Row biến mất khỏi bảng phân công (UI verify)
- KPI counter "Số người ĐG" giảm 1 (UI verify)
- AUDIT_LOG có DELETE (skip — defer DB verify trong Phase B nếu cần audit-trail TC riêng)

> **Note:** Edit hiện tại trong file 03 đã ổn — verify "Row biến mất" + counter là UI-testable, AUDIT_LOG là supplementary nếu admin có UI access /quan-tri/audit-log (cb_nv không access).

---

## TC GIỮ với caveat

### Cảnh báo recon UI 11 tab vs SRS 8 state

Recon log 2026-05-03 ghi nhận app expand 11 tabs filter trạng thái thay vì C10 dropdown (SCR row #6). TC-DG-KH-002 hiện viết theo spec dropdown.

**Quyết định A7:** GIỮ TC theo SRS canonical. Trong Phase B nếu UI thực tế là tabs:
- TC-DG-KH-002 vẫn PASS bằng cách click tab `LAP_KE_HOACH` (filter equivalent)
- Log GAP-MATRIX-A trong report Phase B nếu UI khác spec
- KHÔNG sửa TC theo UI hiện tại vì SRS là source of truth

### TC test data baseline

TC-DG-KH-001/002, DG-PC-001 reference đợt pre-seeded `DG-20260502-0001 Q2/2026` từ recon 6 ngày trước. Phase B Seed step PHẢI verify đợt còn tồn tại + state, hoặc tạo đợt mới qua TC-DG-KH-006 trước.

**Quyết định A7:** GIỮ TC. Phase B handler có trách nhiệm.

---

## Final TC Count per file

| File | Base | A4 edge | A6 fill | A7 LOẠI | Total |
|------|------|---------|---------|---------|-------|
| 01 — Lập KH | 18 | 12 | 0 | 0 | 30 |
| 02 — Tiêu chí | 10 | 6 | 0 | 0 | 16 |
| 03 — Phân công + Duyệt PC | 14 | 6 | 3 | 0 (1 SỬA inline) | 23 |
| 04 — Chấm điểm | 14 | 10 | 3 | 0 | 27 |
| 05 — Báo cáo + Duyệt BC | 14 | 10 | 5 | 0 | 29 |
| 06 — FR-VI-10 | 6 | 2 | 0 | 0 | 8 |
| 07 — Permission Matrix | 8 | 3 | 0 | 0 | 11 |
| **Total** | **84** | **49** | **11** | **0** | **144** |

---

## Acceptance Phase A (pre-Codex)

- ✅ A1 SRS đọc đầy đủ
- ✅ A2 00-test-plan-overview.md
- ✅ A3 7 file UC TC = 84 base
- ✅ A4 49 edge case merge inline + SPEC-CLARIFY-DG-01..07 raised
- ✅ A5 traceability matrix → 10 GAP forward
- ✅ A6 11 fill TC merge inline + 1 SPEC-CLARIFY-DG-07
- ✅ A7 manual UI filter — 0 LOẠI / 1 SỬA inline
- 0 TC chỉ-DB/API thuần
- 144 TC ready for Codex review

**Next:** A8 — `/codex` review TC vs SRS FR-08 + apply patches.
