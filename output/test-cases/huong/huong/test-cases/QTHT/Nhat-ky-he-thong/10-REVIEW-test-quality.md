# A6 Test Review — Quality Score (audit log)

> **Module**: QTHT Nhật ký Hệ thống (FR-VIII-28)
> **Ngày chạy**: 2026-05-08
> **Skill**: bmad-testarch-test-review (manual 6-axis)
> **Output**: Quality score + gap fix mapping (TC mới đã merge inline vào file UC).

---

## 1. 6-Axis Quality Score

| Axis | Mô tả | Score | Note |
|------|-------|-------|------|
| Coverage | BR/AC/Error/Permission/Filter/Output | 9.5/10 | 100% BR + AC + Error + Permission. Output column 75% explicit → fill 3 TC inline. |
| Specificity | TC steps + expected result chi tiết | 9.0/10 | Tất cả TC có cấu trúc STATE/UI/PERSIST. Expected có quote SRS line. |
| Boundary coverage | Bound 89/90/91 + 9999/10K/10001 | 10/10 | Đầy đủ bound on/off cho cả constraint 90 ngày + BR-DATA-06 10K. |
| Independence | Mỗi TC chạy độc lập, có precondition rõ | 9.0/10 | Pre-condition chung file (login QTHT + AUDIT_LOG seed) declare top, các TC reference seed cụ thể. |
| Maintainability | Naming + ID convention | 9.5/10 | TC-NK-NNN với block phân vùng (1xx tra cứu, EXP-xxx export, PERM-xxx permission). Có TraceID link SRS line. |
| Verifiability via MCP | TC chạy được qua chrome-devtools MCP | 9.5/10 | Tất cả qua UI + `list_network_requests` cho verify backend. TC-NK-142/PERM-009 dùng `evaluate_script` trong UI context (A7 OK). |

**Average: 9.42/10** (cao hơn baseline 9.0 cho W2 modules)

---

## 2. Issue List

### 2.1 Gap fixed (đã merge inline ở A6 — 3 TC)

| Issue ID | Mô tả | TC fill (đã merge) | File |
|----------|-------|---------------------|------|
| A5-GAP-01 | Cột "Mã bản ghi" không có TC verify | TC-NK-112 | 01-TC, Section A |
| A5-GAP-02 | Badge màu 7 loại chưa cover đủ | TC-NK-113 | 01-TC, Section A |
| A5-GAP-03 | Empty state khi AUDIT_LOG hoàn toàn trống | TC-NK-124 | 01-TC, Section B |

### 2.2 Open issue (KHÔNG fix — log vào SPEC-CLARIFY hoặc accept)

| Issue ID | Mô tả | Action |
|----------|-------|--------|
| ISSUE-NK-01 | TC-NK-EXP-009 vs EXP-010 phụ thuộc spec final 10K vs 50K | Block ở SPEC-CLARIFY-NHATKY-01 → BA confirm. KHÔNG fix Phase A; Phase B sẽ verify thực tế. |
| ISSUE-NK-02 | TC-NK-139 deleted user behavior phụ thuộc SPEC-CLARIFY-NHATKY-06 | Khi BA confirm → split thành 2 TC nếu cả 2 behavior đều hợp lệ. |
| ISSUE-NK-03 | TC-NK-140 sort badge không bắt buộc theo SRS | Accept; kết quả thực tế sẽ ghi nhận trong execution report (KHÔNG bug nếu không sort được). |
| ISSUE-NK-04 | TC-NK-124 (empty AUDIT_LOG fresh) khó tái hiện trên env shared | Accept P2; defer Phase B nếu không seed được — note trong execution report. |
| ISSUE-NK-05 | TC-NK-EXP-001 dùng filter "tự động hôm nay - 7" — phụ thuộc clock server | Accept; verify timestamp qua MCP. |

### 2.3 Strength

- ✅ Constraint 90 ngày cover đầy đủ on/off bound (TC-NK-134/135/136) — đây là spec mới v3.1 dễ miss.
- ✅ Immutability double-verify (UI ẩn nút TC-141 + BE reject TC-142 + cross-check ở 03-permission TC-008/009).
- ✅ SPEC-CLARIFY có 6 entry rõ ràng (NHATKY-01..06) — sẽ submit BA Phase B.
- ✅ A7 compliance: TC-142/PERM-009 dùng `evaluate_script` trong UI context, KHÔNG curl thuần.
- ✅ Permission cover toàn bộ role hệ thống (QTHT + 3 cấp CB_NV + 3 cấp CB_PD + 4 Tier 2).

---

## 3. TC Distribution

| File | Total | Happy | Negative | Edge |
|------|------:|------:|---------:|-----:|
| 01-TC-tra-cuu-loc-nhat-ky.md | 33 | 13 | 5 | 15 |
| 02-TC-xuat-excel-nhat-ky.md | 12 | 4 | 2 | 6 |
| 03-TC-permission-matrix.md | 9 | 2 | 5 | 2 |
| **Total** | **54** | **19** | **12** | **23** |

**Priority distribution:**
- P0: ~25 (high-risk: auth, immutable, boundary, sanitize)
- P1: ~22
- P2: ~7

---

## 4. SPEC-CLARIFY Pending BA

| ID | File ref | Tóm tắt |
|----|----------|---------|
| NHATKY-01 | 02-TC EXP-009/010 | Excel limit 10K (BR-DATA-06 + AC2) vs 50K (SCR-VIII-10 line 1830). |
| NHATKY-02 | 01-TC TC-NK-106 | Filter Entity (text-input) chỉ có ở SCR-VIII-10 #7, không có trong SRS Inputs section. |
| NHATKY-03 | 01-TC TC-NK-104 | Module list filter chỉ 12 nhãn — thiếu Cấu hình/TKPQ/DM (FR-VIII-01..05). Hay gộp tất cả vào "Quản trị"? |
| NHATKY-04 | 00-overview §5 | Pagination 50/page (SCR-VIII-10 line 1824) khác BR-DATA-07 default 20 — accept vì trong range max 100. |
| NHATKY-05 | 01-TC TC-NK-121 | Spec không nói rõ message khi tu > den. |
| NHATKY-06 | 01-TC TC-NK-139 | Dropdown "Người dùng" có include user `is_deleted=1` không? |

**Total: 6 SPEC-CLARIFY pending BA — sẽ gửi cùng kết thúc Phase A.**

---

## 5. Acceptance per Phase A done criteria (plan §3.1)

| Criteria | Target | Actual | Status |
|----------|--------|--------|--------|
| 7 bước A1-A7 done | ✅ | A1✅ A2✅ A3✅ A4✅ A5✅ A6✅ A7⏳ | ⏳ |
| Traceability ≥95% BR + 100% AC | ≥95%/100% | 100%/100% | ✅ |
| 0 TC chỉ-DB/API thuần | 0 | (sẽ check ở A7) | ⏳ |
| 0 TC sống ở file phụ (08/10/11) | 0 | TC mới A4/A6 đều merged inline | ✅ |
| SPEC-CLARIFY listed | listed | 6 entries | ✅ |

**Pending A7 → mark Phase A done sau khi A7 hoàn tất.**
