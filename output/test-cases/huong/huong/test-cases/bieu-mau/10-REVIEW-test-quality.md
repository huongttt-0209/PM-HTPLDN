# Test Review Quality — FR-09 Biểu mẫu (BMAD A6)

> **Ngày**: 2026-05-06 · **Tool**: bmad-testarch-test-review
> **Scope**: 7 TC files (01-07) + 08 (edge case A4) + 09 (traceability A5)
> **Mục đích**: Đánh giá chất lượng TC theo 6 tiêu chí + đóng 3 gap A5 + chốt ra Phase A done.

---

## 1. Six-axis Quality Score

| Axis | Mô tả | Score 0-10 | Findings |
|------|-------|-----------|----------|
| **Specificity** | Test data + steps đủ chi tiết để chạy độc lập | 9/10 | Hầu hết TC có pre-conditions + test data + expected cụ thể. Trừ điểm: 1-2 TC chỉ ghi "Seed 5 BM" thiếu attribute — chấp nhận được trong A3 vì sẽ fill ở B-Seed. |
| **Coverage breadth** | Happy + Negative + Edge + Auth | 9/10 | Có UI verify, CRUD, security (SQL/XSS), boundary, lifecycle, permission cross-don_vi. Trừ điểm: 2 ERR code chưa cover (BM-04, BM-05) → fix trong A6 dưới đây. |
| **SRS traceability** | TraceID + line ref | 10/10 | Mỗi TC có TraceID kèm `srs-fr-09:line` cụ thể. AC mapping ở 09-traceability rõ ràng. |
| **A7-readiness** | UI/function-testable, không phụ thuộc DB query | 8/10 | Hầu hết qua MCP chrome-devtools được. Còn TC-BM-413 (UC98 verify gián tiếp) — A7 sẽ XÓA per user decision FR-VII-07 LOẠI. |
| **Reusability** | TC độc lập, không phụ thuộc test order ngầm | 7/10 | Một số TC chain (TC-BM-405 cần TC-BM-404 trước) — chấp nhận được vì đã quote precondition rõ. |
| **Maintainability** | Format consistent, sibling-aligned | 9/10 | Format giống CG-TVV/DN. SPEC-CLARIFY ticketed có ID tracking. |

**Tổng score:** 52/60 = **86.7%** → **PASS** (ngưỡng ≥80%).

---

## 2. Issue list + Fix actions

### Issue #1 (P0) — TC-BM-413 (UC98 verify gián tiếp) — REMOVE

**Lý do:** User đã chốt ở 00-test-plan-overview §1.1: "FR-VII-07 (UC98 API) **LOẠI** (A7 — API thuần, không UI)". TC-BM-413 verify network outbound API là test API thuần hóa, vi phạm A7 filter rule §3.1 ("LOẠI: TC require API call thuần").

**Fix:** A7 sẽ Edit 04-TC-quan-ly-bieu-mau.md → xóa TC-BM-413, cập nhật count 14 → 13 TC.

### Issue #2 (P1) — Bổ sung TC-BM-420 (ERR-BM-04 file corrupt)

**Lý do:** A5 traceability gap. ERR-BM-04 nguyên văn "File không hợp lệ hoặc bị hỏng" (srs-fr-09:347) chưa có TC.

**Fix:** Thêm vào 04-TC Section C (Negative).

### Issue #3 (P1) — Bổ sung TC-BM-421 (ERR-BM-05 TM đích không tồn tại)

**Lý do:** A5 gap. ERR-BM-05 nguyên văn "Thư mục đích không tồn tại" (srs-fr-09:348). Trigger khi user mở form thêm BM → TM bị xóa concurrent → submit.

**Fix:** Thêm vào 04-TC Section C (Negative).

### Issue #4 (P1) — Bổ sung TC-BM-401b (UC95 AC5: UPDATE BM kèm replace file)

**Lý do:** A5 AC coverage gap (1/28 AC chưa cover).

**Fix:** Thêm vào 04-TC Section B (Happy CRUD).

### Issue #5 (P2) — Standardize TC ID prefix

**Quan sát:** TC-01 dùng prefix `TC-TM-` (Thư Mục), các file khác dùng `TC-BM-`. Pattern OK vì TM = THU_MUC entity. Giữ nguyên — không refactor (theo principle "không over-engineer").

---

## 3. Action: Edit 04-TC bổ sung 3 TC + xóa TC-BM-413

(Sẽ apply ở A7 — A6 chỉ liệt kê issue; A7 thực thi inline edit + filter.)

---

## 4. Quy trình rà lại sibling consistency (DN, CG-TVV, HD)

| Tiêu chí | DN (`doanh-nghiep/`) | CG-TVV (`CG-TVV/`) | HD (`hoi-dap/`) | BM (`bieu-mau/`) |
|----------|---------------------|--------------------|-----------------|------------------|
| File 00 overview | ✅ | ✅ | ✅ | ✅ |
| Per-FR file split | ✅ | ✅ (14 file UC) | ✅ | ✅ (7 file UC) |
| Permission matrix file | ✅ (06) | (gộp vào 15) | (gộp) | ✅ (07) |
| Edge case review file | ✅ (99) | ✅ (14, 16) | ✅ (edge-case-review-FR02) | ✅ (08) |
| Traceability file | ❌ | ❌ | ❌ | ✅ (09) — **PHỤ THÊM** |
| Test review file | ❌ | ❌ | ❌ | ✅ (10) — **PHỤ THÊM** |

**Quan sát:** BM có thêm 09 + 10 (traceability + review) — pattern đúng BMAD A5/A6. Sibling chưa có vì viết theo workflow cũ (chỉ A1-A4). Đây là enhancement, không cần backport.

---

## 5. Phase A done criteria check (per plan.md §7)

| Criteria | Yêu cầu | Thực tế | Pass? |
|----------|---------|---------|-------|
| 7 bước A1-A7 | Tất cả | A1-A6 done, A7 pending | ⏳ |
| Traceability ≥95% BR | ≥95% | 100% BR + 96.4% AC + 90.5% ERR | ✅ |
| 0 SPEC-CLARIFY pending | 0 hoặc list | 12 ticket — chấp nhận vì A4 đã liệt kê + sẽ gửi BA Phase B | ✅ (với note) |
| 0 TC chỉ-DB/API thuần | 0 | TC-BM-413 còn — A7 sẽ xóa | ⏳ A7 |

**Phase A overall:** Pending A7 confirm → flip ✅.

---

*Generated 2026-05-06 by BMAD A6 (testarch-test-review) — Phase A W2.3 Biểu mẫu*
