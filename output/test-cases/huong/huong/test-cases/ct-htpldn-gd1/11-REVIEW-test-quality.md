# A6 — Test Review (6-axis quality) — CT HTPLDN GĐ1

> **Ngày**: 2026-05-06 · **Tool**: bmad-testarch-test-review
> **Scope**: 8 TC files (01-08), 83 TC sau A4 → 86 TC sau A6 fill gap
> **Mục đích**: Đánh giá chất lượng TC theo 6 axis + fill gap từ A5 (inline merge vào file UC).

---

## 1. 6-axis quality score

| Axis | Định nghĩa | Score | Note |
|------|-----------|-------|------|
| Test Independence | Mỗi TC độc lập, không chạy chuỗi | 9/10 | TC-LC-011 cross-phase đặc thù. TC-LC-016/017 cycle là intentional (verify cycle). |
| Atomic Assertions | 1 TC = 1 expected behavior | 8/10 | Đa số TC tốt. Một số TC (TC-LC-001) gộp 3 assertion (state + audit + notification). Acceptable cho lifecycle. |
| Boundary Coverage | BVA: min/max/equal/off-by-one | 9/10 | A4 thêm boundary: ngan_sach=0, thoi_gian equal, page_size > 100. |
| Negative Path | TC negative đầy đủ cho mọi error code | 10/10 | Đủ ERR-XI-01-* / ERR-XI-04-* / ERR-XI-05-* / ERR-XI-05a-* |
| State/Permission Coverage | Mọi role × action × state guard | 9/10 | File 08 cover permission cross. TC-PD-CT-005 mark SPEC-CLARIFY-CT-01 (cross-đơn vị cùng cấp). |
| Spec Traceability | TraceID quote SRS line | 10/10 | Mọi TC có `FR-XI-XX / {section}` traceID. |

**Composite score:** (9+8+9+10+9+10) / 6 = **9.17/10** ⭐

---

## 2. Issues Found

### Issue 1 — TC-LC-011 (Hoàn thành happy) cross-phase dependency
**Severity:** Medium
**Mô tả:** TC require pre-seed 1 đợt BC ở DA_TONG_HOP — state này chỉ đạt sau full cycle GĐ2 (Lập BC → Phê duyệt → Gửi TW → Tổng hợp).
**Action A6:** Đã có note trong file 03 + Gap report. Phase B sẽ phải seed thủ công cross-phase HOẶC defer. Giữ TC làm spec coverage.

### Issue 2 — Audit log TC dedicated thiếu (GAP-CT-A5-03)
**Severity:** Low
**Mô tả:** BR-DATA-05 áp dụng cho mọi action lifecycle — hiện rải rác trong expected của 18 TC. Thiếu 1 TC dedicated verify chi tiết cấu trúc audit log (action_type, actor, timestamp, before/after).
**Action A6:** Thêm 1 TC `TC-CT-AUDIT-001` vào file 01 Section C — verify audit log entry sau 1 cycle Tạo→Sửa→Xóa.

### Issue 3 — Rollback Cổng PLQG verify state DB (GAP-CT-A5-05)
**Severity:** Medium
**Mô tả:** TC-CB-CT-002 mention rollback nhưng expected chỉ "Trạng thái rollback → DA_DUYET". Thiếu verify reload page sau rollback vẫn DA_DUYET (đảm bảo state KHÔNG transient persist DA_CONG_BO).
**Action A6:** Edit TC-CB-CT-002 strengthen expected: "Reload page → vẫn DA_DUYET. Network call thứ 2 GET CT → response.trang_thai=DA_DUYET, la_cong_bo=0".

### Issue 4 — Notification TC riêng thiếu (GAP-CT-A5-02)
**Severity:** Low
**Mô tả:** Notification gửi CB PD cùng cấp khi trình PD chỉ verify trong TC-TR-CT-002 (notification chỉ scope cùng cấp). Chưa có TC verify NV nhận notification khi PD duyệt/từ chối.
**Action A6:** Thêm 1 TC `TC-PD-CT-010` vào file 05 — verify NV nhận notification khi PD duyệt thành công.

### Issue 5 — TC-PD-CT-005 SPEC-CLARIFY chưa có expected fallback
**Severity:** Low
**Mô tả:** TC mark SPEC-CLARIFY-CT-01 nhưng expected mơ hồ ("403 hoặc ERR-XI-04-03 tùy tổ chức rule"). Phase B run sẽ không biết đâu là PASS.
**Action A6:** Edit TC-PD-CT-005: prefer expected (1) là **403 / scope BR-AUTH-08** (đơn vị khác → không thấy CT). Mark prefer + alternatives + B-Verify dùng 2-source check.

---

## 3. Gap Fill (inline merge — Iron Rule §3.1)

A6 thêm 3 TC mới:
- `TC-CT-AUDIT-001` → file `01-TC-quan-ly-ct-CRUD.md` Section C Edge
- `TC-PD-CT-010` → file `05-TC-phe-duyet-ct.md` Section A Happy
- (TC-CB-CT-002 strengthen: edit expected only — không TC mới)

A6 edit 1 TC existing:
- `TC-PD-CT-005` strengthen expected (clarify primary vs alt)

---

## 4. Tổng kết A6

- **Composite score**: 9.17/10 ⭐
- **Issues**: 5 (1 Medium + 4 Low)
- **TC mới**: 2 (audit + notification PD)
- **TC sửa**: 2 (TC-CB-CT-002, TC-PD-CT-005)
- **Total Phase A TC sau A6**: 83 + 2 = **85 TC**

*Generated 2026-05-06 — Phase A step A6 audit log*
