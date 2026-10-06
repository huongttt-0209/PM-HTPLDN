# A6 Test Review — Quality Score (audit log)

> **Module**: QTHT Cấu hình Hệ thống (SCR-VIII-06 + FR-VIII-29)
> **Ngày chạy**: 2026-05-08
> **Skill**: bmad-testarch-test-review (manual 6-axis)
> **Output**: Quality score + gap fix mapping (TC mới đã merge inline vào file UC).

---

## 1. 6-Axis Quality Score

| Axis | Mô tả | Score | Note |
|------|-------|-------|------|
| Coverage | BR/AC/Error/Permission/SM/Output field | 9.2/10 | BR 97% + AC 92% (sau fill, 1 SPEC-CLARIFY còn lại) + Error 100% + Permission 100% + SM 100% + Output 91%. AC FR-VIII-29 AC3 (Calendar view) optional pending BA. |
| Specificity | TC steps + expected result chi tiết | 9.0/10 | Tất cả TC có cấu trúc STATE/UI/PERSIST. Quote SRS line. Tab 3 (Mô hình B) đặc biệt chi tiết với cross-cấp/cross-don_vi cases. |
| Boundary coverage | Bound CB1<CB2<100, ten_mau 200/201, noi_dung 10K, thoi_han 1/999, ket_thuc=bat_dau | 9.5/10 | Đầy đủ bound on/off cho mọi numeric/text field. |
| Independence | Mỗi TC chạy độc lập, có precondition rõ | 9.0/10 | Pre-condition seed 9 mẫu TW/BN/DP + 5 ngày lễ + 4 SLA seed declare ở overview. |
| Maintainability | Naming + ID convention | 9.5/10 | TC-CH-{SLA/MPH/PC/QT/NL/PERM}-NNN với block phân vùng rõ. TraceID link SRS line. |
| Verifiability via MCP | TC chạy được qua chrome-devtools MCP | 9.5/10 | Tất cả qua UI + `evaluate_script` cho IDOR/cross-cấp BE direct (UI bridge OK). |

**Average: 9.28/10** (cao hơn baseline 9.0; gần với W1.1 Nhật ký HT 9.42)

---

## 2. Issue List

### 2.1 Gap fixed (đã merge inline ở A6 — 7 TC)

| Issue ID | Mô tả | TC fill (đã merge) | File |
|----------|-------|---------------------|------|
| A5-GAP-CH-01 | FR-VIII-10 AC2 "Thêm mới cấu hình SLA" — chưa cover | TC-CH-SLA-007 | 01-TC-tab-sla.md, Section A |
| A5-GAP-CH-02 | ERR-SLA-03 (loại YC duplicate) — chưa cover | TC-CH-SLA-008 | 01-TC-tab-sla.md, Section A (paired với GAP-01) |
| A5-GAP-CH-03 | Toggle gui_thong_bao_app | TC-CH-SLA-009 | 01-TC-tab-sla.md, Section B |
| A5-GAP-CH-04 | Field tu_khoa happy + dùng search | TC-CH-MPH-007 | 03-TC-tab-mau-phan-hoi.md, Section A |
| A5-GAP-CH-05 | Field mo_ta happy | TC-CH-MPH-008 | 03-TC-tab-mau-phan-hoi.md, Section A |
| A5-GAP-CH-06 | Field mo_ta ngày lễ happy | TC-CH-NL-006 | 05-TC-ngay-le.md, Section A |
| A5-GAP-CH-07 | Empty state khi filter no-match | TC-CH-MPH-050 | 03-TC-tab-mau-phan-hoi.md, Section E |

### 2.2 Open issue (KHÔNG fix — log vào SPEC-CLARIFY hoặc accept)

| Issue ID | Mô tả | Action |
|----------|-------|--------|
| ISSUE-CH-01 | Tab 2 SCR-VIII-06 spec mâu thuẫn (UI render vs FR đã bỏ) — TC-CH-PC-001 verify thực tế | SPEC-CLARIFY-CAUHINH-01 — chờ BA. |
| ISSUE-CH-02 | Tab 4 spec field detail thiếu (ten_buoc, SLA per-step, phan_cong_tu_dong) | SPEC-CLARIFY-CAUHINH-02 + 08 — defer detailed validation đến khi BA cung cấp. |
| ISSUE-CH-03 | Cột "QH nghiêm trọng (%)" chỉ có ở SCR-VIII-06 #10, không có ở FR-VIII-10 Inputs | SPEC-CLARIFY-CAUHINH-03 — TC-CH-SLA-006 chờ verify. |
| ISSUE-CH-04 | FR-VIII-10 AC2 vs schema enum 4 cố định — mâu thuẫn | TC-CH-SLA-007 chờ Phase B verify. |
| ISSUE-CH-05 | Calendar view FR-VIII-29 AC3 — optional hay mandatory? | SPEC-CLARIFY-CAUHINH-06 — TC-CH-NL-030 P2. |
| ISSUE-CH-06 | Race condition Tab 1 SLA save vs HS create (TC-CH-SLA-022) | SPEC-CLARIFY-CAUHINH-07 — defer Phase B. |
| ISSUE-CH-07 | Filter "Phạm vi" cho TW user (đã có quyền toàn quốc) ý nghĩa gì? | SPEC-CLARIFY-CAUHINH-04 — TC-CH-MPH-040 verify. |
| ISSUE-CH-08 | Import Excel ngày lễ limit (10K?) | SPEC-CLARIFY-CAUHINH-05 — TC-CH-NL-023. |

### 2.3 Strength

- ✅ **Mô hình B Hybrid 2 tầng** cover toàn diện: 3 cấp × CRUD × Scope rules + UI auto-fill bypass via API + cross-cấp + cross-don_vi ngang.
- ✅ **Snapshot pattern** v3.1 cover đầy đủ Tab 1 + Tab 4 với 6 TC e2e (HS cũ giữ / HS mới áp / race condition / reload không nhảy).
- ✅ **Integration BR-CALC-03** (TC-CH-NL-040) — verify e2e SLA tính trừ ngày lễ; đây là PURPOSE chính của module Ngày lễ.
- ✅ **8 SPEC-CLARIFY** rõ ràng — sẽ submit BA Phase B (cao hơn baseline 6 của W1.1).
- ✅ **A7 compliance**: tất cả IDOR/direct API TC dùng `evaluate_script` UI context, KHÔNG curl thuần.
- ✅ **FR-II-NEW-01 deprecation** (Tab 2) verify behavior thực tế thay vì silent skip — phòng case BA chưa update spec.

### 2.4 Weakness / Limitations

- ⚠️ Tab 4 Quy trình hỗ trợ chỉ có 12 TC vì SPEC-CLARIFY-CAUHINH-08 (spec field thiếu). Phase B sẽ có thể phát hiện nhiều bug detailed validation chưa cover.
- ⚠️ FR-VIII-29 AC3 Calendar view chỉ 1 TC P2 vì spec ghi "tùy chọn" — nếu BA confirm mandatory cần fill thêm.
- ⚠️ Output column field coverage 91% (mo_ta partial trên Tab 3 + tu_khoa partial) — một số field chỉ test happy không có edge case riêng.

---

## 3. TC Distribution

| File | Total | Happy | Negative | Edge |
|------|------:|------:|---------:|-----:|
| 01-TC-tab-sla.md | 27 | 8 | 7 | 12 |
| 02-TC-tab-phan-cong-deprecated.md | 3 | 0 | 2 | 1 |
| 03-TC-tab-mau-phan-hoi.md | 41 | 19 | 9 | 13 |
| 04-TC-tab-quy-trinh-ho-tro.md | 12 | 4 | 3 | 5 |
| 05-TC-ngay-le.md | 22 | 6 | 5 | 11 |
| 06-TC-permission-matrix.md | 19 | 7 | 8 | 4 |
| **Total** | **124** | **44** | **34** | **46** |

**Priority distribution:**
- P0: ~62 (~50% — high-risk: Mô hình B scope, snapshot, immutable, cross-cấp BE check)
- P1: ~52
- P2: ~10

---

## 4. SPEC-CLARIFY Pending BA

| ID | File ref | Tóm tắt |
|----|----------|---------|
| CAUHINH-01 | 02-TC-tab-phan-cong | Tab 2 ẨN hay deprecation banner? FR-II-NEW-01 đã bỏ Q11. |
| CAUHINH-02 | 04-TC-tab-quy-trinh-ho-tro | SCR ghi `FR-VIII-25` (VNeID) — không khớp Tab 4 Quy trình. FR thực tế nào? |
| CAUHINH-03 | 01-TC-tab-sla TC-006 | Cột QH-NT 200% chỉ có ở SCR, không có Inputs FR-VIII-10. v3.1 mới? |
| CAUHINH-04 | 03-TC-tab-mau-phan-hoi TC-040 | Filter "Phạm vi" cho TW user (đã có quyền toàn quốc) ý nghĩa gì? |
| CAUHINH-05 | 05-TC-ngay-le TC-023 | Import Excel ngày lễ limit bao nhiêu? Format file? Header? |
| CAUHINH-06 | 05-TC-ngay-le TC-030 | Calendar view optional hay mandatory? |
| CAUHINH-07 | 01-TC-tab-sla TC-022 | Race condition save SLA + create HS cùng giây — config nào áp? |
| CAUHINH-08 | 04-TC-tab-quy-trinh-ho-tro | Spec field detail Tab 4 thiếu (ten_buoc / SLA per-step / phan_cong_tu_dong). |

**Total: 8 SPEC-CLARIFY pending BA — sẽ gửi cùng kết thúc Phase A.**

---

## 5. Acceptance per Phase A done criteria (plan §3.1)

| Criteria | Target | Actual | Status |
|----------|--------|--------|--------|
| 7 bước A1-A7 done | ✅ | A1✅ A2✅ A3✅ A4✅ A5✅ A6✅ A7⏳ | ⏳ |
| Traceability ≥95% BR + 100% AC | ≥95%/100% | 97%/92.3% (AC FR-VIII-29 AC3 partial pending BA) | ⚠️ partial — chấp nhận vì SPEC-CLARIFY |
| 0 TC chỉ-DB/API thuần | 0 | (A7 sẽ verify) | ⏳ |
| 0 TC sống ở file phụ (08/10/11) | 0 | TC mới A4/A6 đều merged inline | ✅ |
| SPEC-CLARIFY listed | listed | 8 entries | ✅ |

**Pending A7 → mark Phase A done sau khi A7 hoàn tất.**
