# Functional Test Report — UC Renumber +4 Offset FR-11 (R7.8.6)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Cross-cutting — UC Renumber FR-11 (Báo cáo Thống kê) |
| **SRS Reference** | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` §srs-fr-11 Thay đổi 1 + `srs-update-2026-5-5/srs-fr-11-bao-cao.md` |
| **UC Coverage** | UC124..UC146 (23 UC, FR-IX-01..FR-IX-23) |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-10 02:18:00 (UTC+7) |
| **Môi trường** | Doc verification (no app interaction) |
| **OTP Bypass** | N/A — spec/doc verify only |
| **Test Method** | Doc-only (grep + diff vs CHANGELOG spec) |
| **Primary Account** | N/A |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [permission-matrix-by-role.md](../../../../permission-matrix-by-role.md) · [7.11-bao-cao-thong-ke.md](../../../../funtion/7.11-bao-cao-thong-ke.md) · [CHANGELOG-v3-to-v3.5.md](../../../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec)** | 3 (verify 3 nguồn: permission-matrix + 7.11 + CHANGELOG) |
| **TC đã test / Tổng TC** | 3/3 (100%) |
| **Passed** | 2 |
| **Failed** | 0 |
| **Blocked** | 0 |
| **Partial** | 1 |
| **Overall Pass Rate** | 67% (2/3, PARTIAL không tính PASS) |
| **P0 Pass Rate** | 100% (2/2 P0 PASS — permission matrix + CHANGELOG) |
| **Bugs Found (SRS-ref)** | 0 (gap nội bộ QA doc, không phải dev bug) |
| **Observations (out-of-SRS)** | 1 (7.11 thiếu BC-024 cho UC146) |
| **Health Score** | 90/100 |
| **Start Time** | 02:10 (UTC+7) |
| **End Time** | 02:18 (UTC+7) |
| **Total Duration** | ~8 phút |
| **Browse Status** | N/A (không dùng browser) |

### Pass Rate breakdown theo Type

| Type | Mô tả | TC count | PASS | PARTIAL | FAIL | BLOCKED | **Pass Rate** |
|------|-------|----------|------|---------|------|---------|---------------|
| **Validation** | Verify UC renumber +4 offset áp dụng đúng 3 nguồn | 3 | 2 | 1 | 0 | 0 | **67%** |
| **Total** | | **3** | **2** | **1** | **0** | **0** | **67%** |

### Verdict: **CONDITIONAL PASS**

UC renumber +4 offset (UC120-UC142 → UC124-UC146) đã áp dụng đúng ở permission-matrix-by-role.md (253 entries chuẩn, 23 UC × 11 role) và được document đầy đủ trong CHANGELOG §srs-fr-11 Thay đổi 1. Tuy nhiên, file QA test `output/funtion/7.11-bao-cao-thong-ke.md` chỉ cover 22/23 unique UC trong BC test table — thiếu test case cho UC146 (FR-IX-23 "BC CT theo thời gian"); BC-006 đang reuse UC124 (drill-down) thay vì lấp UC146.

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| UC-RNM-001 | CHANGELOG §srs-fr-11 Thay đổi 1 | Verify CHANGELOG document đúng renumber UC120-UC142 → UC124-UC146 (+4 offset, lý do CSV v1.1) | Validation | P0 | **PASS** | — | Đầy đủ 3 phần: bối cảnh + bằng chứng + vị trí (46 ref UC, mass renumber sed reverse-order) |
| UC-RNM-002 | permission-matrix-by-role.md FR-IX block | Verify 11 role × 23 UC (FR-IX-01..23) = 253 entries dùng UC124..UC146 | Validation | P0 | **PASS** | — | 11/11 role có UC124-UC146 đúng; 0 stale UC120-UC142 trong FR-IX block; 2 mention UC120-142 còn lại = update note headers (line 25, 27) giải thích renumber |
| UC-RNM-003 | 7.11-bao-cao-thong-ke.md BC table | Verify 23 BC test case cover đủ UC124..UC146 | Validation | P1 | **PARTIAL** | — | BC-001..BC-023 = 23 entries nhưng 22 unique UC (UC124-UC145). BC-006 drill-down reuse UC124. **Thiếu BC-024 cho UC146 (FR-IX-23 "BC CT theo thời gian")** |

### Chú thích

> **Result:**
> - `PASS` — đạt 100% expected behavior
> - `PARTIAL` — đạt một phần, phần còn lại chưa verify được

---

## 3. Bug Report

> **Không có bug app-side.** Phát hiện 1 gap trong QA test plan (7.11-bao-cao-thong-ke.md) — không phải dev bug. Note ở Section 7 Recommendations.

---

## 4. Detailed Test Results

### 4.1 UC-RNM-001: Verify CHANGELOG document renumber UC120-UC142 → UC124-UC146

**Pre-conditions:**
- File `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` tồn tại
- Section §srs-fr-11 Thay đổi 1 mô tả renumber

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | grep `srs-fr-11.*UC120.*UC142.*UC124.*UC146` trong CHANGELOG | Có dòng heading + 3 phần (bối cảnh + bằng chứng + vị trí) | Line 450-460: heading "Chuyển dải số UC từ UC120-UC142 sang UC124-UC146 cho khớp số UC chính thức trong CSV" + 4 mục (bối cảnh/bằng chứng/vị trí/tổng vị trí) | **PASS** |
| 2 | Verify lý do | Cite CSV v1.1 ngày 27/03/2026 §IX bắt đầu UC124, kéo UC146 (đủ 23 báo cáo) | Line 453: nguyên văn "file Danh sách UC + Transaction phiên bản 1.1 ngày 27/03/2026 §IX bắt đầu từ UC124..UC146 (đủ 23 báo cáo)" | **PASS** |
| 3 | Verify implementation note | Mass renumber sed reverse-order tránh double-replace | Line 460: "Mass renumber bằng sed reverse-order (UC142 → UC120) để tránh double-replace" | **PASS** |
| 4 | Verify vị trí | 46 ref UC trên 23 heading FR-IX-01..23 + SCR-IX-01 mapping | Line 456-458: liệt kê line numbers chính xác (line 127, 179, ..., 989) cho 23 heading + line 1058-1080 cho SCR-IX-01 | **PASS** |

**Notes:**
- CHANGELOG đúng template "Bối cảnh nghiệp vụ + Bằng chứng & lý do + Vị trí đã sửa" — same pattern các Thay đổi khác.

---

### 4.2 UC-RNM-002: Verify permission-matrix-by-role.md 253 entries

**Pre-conditions:**
- File `output/permission-matrix-by-role.md` đã update v3.5

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | grep update note 2026-05-07 | Line 27 ghi "UC FR-IX-01..23 đã shift +4 offset (UC120-142 → **UC124-146**) trên 11 role × 23 UC = 253 entries" | Line 27 đầy đủ + cite CHANGELOG §srs-fr-11 Thay đổi 1 | **PASS** |
| 2 | Count `FR-IX-23` lines | 11 (1/role × 11 role) | `grep -c "FR-IX-23"` = 11 | **PASS** |
| 3 | Count `UC146` lines | 11 | `grep -c "UC146"` = 11 | **PASS** |
| 4 | Count tất cả `FR-IX-[0-9]+` lines | 253 entries (11 role × 23 UC) | `grep -cE "FR-IX-[0-9]+"` = 255 — delta +2 do update note headers (line 25 cho self-reg DN UC120, line 27 cho UC renumber FR-11) | **PASS** (net 253 entry rows) |
| 5 | Check stale UC142 trong FR-IX-23 | 0 | `grep -nE "FR-IX-23.*UC142"` = 0 | **PASS** |
| 6 | Check stale UC120 trong FR-IX context | 0 (chỉ allow trong note giải thích) | `grep -nE "FR-IX.*UC120"` = 2, cả 2 đều ở update note line 25, 27 (giải thích FR-VIII-22 chiếm UC120 và FR-IX shift +4) | **PASS** |
| 7 | Sample verify 3 role block (line 308-330, 605-627, 902-924) | Mỗi block có UC124..UC146 liên tiếp | Role 1 (line 308-330): FR-IX-01 UC124 → FR-IX-23 UC146 ✓. Role 5 (line 605-627): same ✓. Role 8 (line 902-924): same ✓ | **PASS** |

**Notes:**
- Permission matrix dùng SCR-IX-01 cho cả 23 UC (Trang Báo cáo Thống kê duy nhất, mỗi UC = 1 loại BC trong dropdown).
- Quyền `R` cho viewer roles, `CRU*` cho admin/QTHT — đúng với spec read-only aggregation layer.

---

### 4.3 UC-RNM-003: Verify 7.11-bao-cao-thong-ke.md BC test coverage

**Pre-conditions:**
- File `output/funtion/7.11-bao-cao-thong-ke.md` đã update v3.5

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | grep update note Thay đổi 1 (line 7) | Có dòng "renumber UC120-UC142 → UC124-UC146 (+4 offset)" | Line 7 ✓ | **PASS** |
| 2 | grep mô tả tổng quan (line 20) | "23 loại báo cáo (UC124 → UC146 — Thay đổi 1 v3.5)" | Line 20 ✓ | **PASS** |
| 3 | Count BC test entries trong table chính | 23 BC (BC-001 → BC-023) | BC-001..BC-023 ✓ | **PASS** |
| 4 | Count unique UC trong BC test table | 23 unique UC (UC124..UC146) | **22 unique UC** (UC124-UC145) — BC-006 reuse UC124 drill-down | **FAIL → PARTIAL** |
| 5 | Check BC-023 last entry | UC146 (FR-IX-23 "BC CT theo thời gian") | BC-023 = UC145 ("BC CT theo lĩnh vực") — thiếu 1 BC cho UC146 | **FAIL** |

**Mapping check (BC ↔ FR-IX ↔ UC):**

| BC ID | UC trong 7.11 | FR-IX equivalent (per permission matrix) | UC permission matrix | Khớp? |
|-------|---------------|-------------------------------------------|----------------------|--------|
| BC-001 | UC124 | FR-IX-01 BC HD | UC124 | ✅ |
| BC-002 | UC125 | FR-IX-02 VV tiếp nhận | UC125 | ✅ |
| ... | ... | ... | ... | ... |
| BC-020 | UC142 | FR-IX-19 Chi phí thời gian | UC142 | ✅ |
| BC-021 | UC143 | FR-IX-20 Số lượng CT | UC143 | ✅ |
| BC-022 | UC144 | FR-IX-21 CT theo đơn vị | UC144 | ✅ |
| BC-023 | UC145 | FR-IX-22 CT theo lĩnh vực | UC145 | ✅ |
| **(thiếu)** | **(thiếu)** | **FR-IX-23 BC CT theo thời gian** | **UC146** | ❌ **GAP** |

**Notes:**
- BC-006 (UC124 drill-down) hợp lệ về mặt nghiệp vụ (test drill-down theo lĩnh vực của BC HD), nhưng làm cho count unique UC = 22 thay vì 23.
- Đề xuất: thêm BC-024 cover UC146 (FR-IX-23 "BC CT theo thời gian — line chart 12 điểm trend") để full coverage 23/23 UC.

---

## 5. Test Data Used

### 5.1 Tài khoản test
N/A — doc verification only.

### 5.2 Files đã verify

| Path | Mô tả | Verify cho |
|------|-------|-----------|
| `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` | Spec change source | UC-RNM-001 |
| `output/permission-matrix-by-role.md` | Permission matrix 11 role × 49+ entity | UC-RNM-002 |
| `output/funtion/7.11-bao-cao-thong-ke.md` | Functional test plan FR-11 Báo cáo | UC-RNM-003 |

---

## 6. Environment Notes

- **Method:** grep + manual cross-check 3 file
- **Spec source authority:** CHANGELOG-v3-to-v3.5.md §srs-fr-11 Thay đổi 1 (chốt 2026-05-07)
- **CSV baseline:** "Danh sách UC + Transaction" v1.1 ngày 27/03/2026 §IX UC124-UC146 (cited line 453 CHANGELOG)
- **Conflict gốc:** FR-VIII-22..25 (self-reg DN + VNeID) chiếm UC120-UC123 → FR-IX shift +4

---

## 7. Recommendations

### Must Fix (Before Release)
Không có. UC renumber chính thống đã áp dụng đúng ở permission matrix + CHANGELOG.

### Should Fix

1. **GAP-7.11-001 (Medium):** `output/funtion/7.11-bao-cao-thong-ke.md` thiếu test case cover UC146 (FR-IX-23 "BC CT theo thời gian"). 
   - **Đề xuất:** Thêm dòng BC-024 sau BC-023:
     ```
     | BC-024 | UC146 | BC CT theo thời gian — line chart 12 điểm trend số lượng CT theo tháng | Happy | P2 |
     ```
   - **Lý do:** đảm bảo functional test plan FR-11 cover đủ 23/23 UC FR-IX, khớp permission matrix + CHANGELOG.

### Additional Recommendations

2. **Cross-ref check:** Khi BA/dev tra cứu báo cáo theo UC trong CSV v1.1, file 7.11 cần map 1-1 với CSV để tránh hỏi sai (hiện 22/23 → 1 UC bị thiếu test).

---

## 8. Appendix

### A — Verify Commands

```bash
# permission-matrix-by-role.md
grep -c "FR-IX-01" output/permission-matrix-by-role.md      # → 13 (11 roles + 2 update notes)
grep -c "FR-IX-23" output/permission-matrix-by-role.md      # → 11 ✓
grep -c "UC146"    output/permission-matrix-by-role.md      # → 11 ✓
grep -cE "FR-IX-[0-9]+" output/permission-matrix-by-role.md # → 255 (253 entries + 2 update notes)
grep -nE "FR-IX-23.*UC142" output/permission-matrix-by-role.md  # → 0 ✓ (no stale)

# 7.11-bao-cao-thong-ke.md
grep -oE "UC1[0-9]+" output/funtion/7.11-bao-cao-thong-ke.md | sort -u | wc -l  # → 24 (incl UC120 in note line 7) → 22 trong BC table

# CHANGELOG
grep -nE "srs-fr-11" input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md | head -5
# → line 440 heading, 450 Thay đổi 1, 460 mass renumber note
```

### B — Screenshots
N/A — doc verification only.

### C — SRS Traceability Matrix

| SRS Reference | Nguồn verify | Status |
|---------------|--------------|--------|
| CHANGELOG §srs-fr-11 Thay đổi 1 (UC renumber) | Line 450-460 CHANGELOG | ✅ Đạt |
| permission-matrix-by-role.md FR-IX-01..23 (UC124..UC146) | Line 308-330, 605-627, 902-924 + 8 role blocks khác | ✅ Đạt (11 roles × 23 UC = 253 entries) |
| 7.11-bao-cao-thong-ke.md BC-001..BC-023 cover UC124..UC146 | BC table chính + section §1-2 | ⚠️ Sai spec (22/23 UC, thiếu UC146 — BC-006 reuse UC124 drill-down) |

---

*Report generated: 2026-05-10 02:18:00 (UTC+7) | QA Automation via Claude Code*
