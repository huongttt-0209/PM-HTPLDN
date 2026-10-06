# Edge Case Hunter Review — FR-09 Biểu mẫu (BMAD A4) — MERGE AUDIT LOG

> **Ngày**: 2026-05-06 · **Reviewer**: BMAD edge-case-hunter
> **Status**: ✅ **MERGED 2026-05-06** — 21 edge case proposed đã inline merge vào 7 file UC (01-07).
> **File này KHÔNG còn là TC source** — chỉ là audit history "đã merge gì vào đâu". Phase B B-block KHÔNG ref file này.

---

## Quy ước cũ (giữ làm reference)

| Severity | Action |
|----------|--------|
| 🔴 P0 | Bắt buộc merge vào file UC |
| 🟡 P1 | Nên merge — bug khả năng cao |
| 🟢 P2 | Optional — nice-to-have |

---

## 1. Merge mapping (proposal → final TC ID trong file UC)

| Original ID (proposal) | Severity | Mô tả | Merge target file | Final TC ID | Section |
|-----------------------|----------|-------|-------------------|-------------|---------|
| TC-BM-111 | 🟡 P1 | Whitespace trailing/leading `"  HĐ LĐ  "` | 01-TC-quan-ly-thu-muc.md | **TC-TM-023** | C. Edge |
| TC-BM-112 | 🟡 P1 | Mô tả TM boundary 2000 ký tự | 01 | **TC-TM-024** | C. Edge |
| TC-BM-113 | 🟢 P2 | thu_tu_hien_thi out of range 0/21 | 01 | **TC-TM-025** | C. Edge |
| TC-BM-114 | 🟡 P1 | Concurrent CREATE 2 tab race | 01 | **TC-TM-026** | C. Edge |
| TC-BM-208 | 🟢 P2 | Vietnamese Unicode `"Lê Văn"` | 02-TC-tim-kiem-thu-muc.md | **TC-BM-208** | C. Security & Edge |
| TC-BM-209 | 🟡 P1 | SQL LIKE wildcard escape `%` `_` | 02 | **TC-BM-209** | C. Security & Edge |
| TC-BM-210 | 🟢 P2 | Keyword exactly 200 ký tự (BR-EC-13 boundary) | 02 | **TC-BM-210** | C. Security & Edge |
| TC-BM-308 | 🔴 P0 | SM transition AN → CONG_KHAI re-publish | 03-TC-cong-khai-thu-muc.md | **TC-BM-308** | A. Publish Happy Path |
| TC-BM-309 | 🟡 P1 | API Cổng PLQG timeout vs 500 | 03 | **TC-BM-309** | B. Negative |
| TC-BM-415 | 🔴 P0 | Tên BM boundary 500 ký tự | 04-TC-quan-ly-bieu-mau.md | **TC-BM-415** | C. Negative |
| TC-BM-416 | 🟡 P1 | File extension `.DOCX` case-insensitive | 04 | **TC-BM-416** | C. Negative |
| TC-BM-417 | 🔴 P0 | XSS payload trong rich-text `mo_ta_cong_khai` | 04 | **TC-BM-417** | C. Negative |
| TC-BM-418 | 🟡 P1 | Switch ON no upload ảnh đại diện → default | 04 | **TC-BM-418** | A. UI / Happy |
| TC-BM-419 | 🔴 P0 | Cascade delete BM CONG_KHAI (gọi API gỡ Cổng) | 04 | **TC-BM-419** | D. Edge |
| TC-BM-507 | 🟡 P1 | Search exact mã BM vs LIKE substring | 05-TC-tim-kiem-bieu-mau.md | **TC-BM-507** | A. Search Happy |
| TC-BM-508 | 🟢 P2 | Multi-filter empty intersection | 05 | **TC-BM-508** | B. Negative |
| TC-BM-608 | 🟡 P1 | Excel metadata mismatch số file content | 06-TC-import-hang-loat.md | **TC-BM-608** | C. Negative |
| TC-BM-609 | 🟡 P1 | Duplicate file names trong batch | 06 | **TC-BM-609** | C. Negative |
| TC-BM-610 | 🟢 P2 | Excel metadata file > 5MB boundary | 06 | **TC-BM-610** | C. Negative |
| TC-BM-PERM-007 | 🟡 P1 | CB_NV_BN_A vs BN_B ngang cấp isolation | 07-TC-permission-matrix.md | **TC-BM-PERM-007** | B. Negative |
| TC-BM-PERM-008 | 🟡 P1 | DN download BM CONG_KHAI qua Cổng PLQG | 07 | **TC-BM-PERM-008** | A. Happy |

**Tổng: 21 edge case → 100% merged inline vào 7 file UC.**

---

## 2. Reasoning từng case (giữ làm history)

### EC-01: File 01 (Quản lý thư mục) — 4 case

- **TC-TM-023 (was TC-BM-111)**: A3 chưa cover whitespace handling. Backend có trim hay không? Nếu không trim → trùng tên với "HĐ LĐ" hiện tại sẽ ERR-TM-01 nhầm. SPEC-CLARIFY-BM-11.
- **TC-TM-024 (was TC-BM-112)**: A3 chỉ test ten_thu_muc max 500, mô tả max 2000 (srs-fr-09:610) chưa test boundary.
- **TC-TM-025 (was TC-BM-113)**: SRS line 91 quote "1-20" — boundary 0 và 21 cần verify reject.
- **TC-TM-026 (was TC-BM-114)**: A3 đã test optimistic lock UPDATE (TC-BM-109), thiếu race CREATE.

### EC-02: File 02 (Tìm kiếm thư mục) — 3 case

- **TC-BM-208**: A3 chưa test Unicode boundary — sibling CG-TVV TC-CG-122 đã có pattern.
- **TC-BM-209**: Sibling CG-TVV TC-CG-115. Nếu BE không escape `%` `_` → match toàn bộ records.
- **TC-BM-210**: A3 chỉ test sanitize (TC-BM-206/207), chưa test boundary 200 chính xác.

### EC-03: File 03 (Công khai thư mục) — 2 case

- **TC-BM-308 (P0)**: TC-BM-302 test CONG_KHAI→AN, thiếu chiều ngược. SM-BIEUMAU srs-fr-09:826 nguyên văn "AN → CONG_KHAI".
- **TC-BM-309**: TC-BM-305 test 500 error, thiếu timeout case (BR-EC-20 transactional consistency).

### EC-04: File 04 (Quản lý biểu mẫu) — 5 case

- **TC-BM-415 (P0)**: A3 chỉ test ten_thu_muc 500 (TC-TM-012/020), tên BM cũng max 500 (srs-fr-09:295) → cần TC riêng.
- **TC-BM-416**: SRS quote `IN ('doc','docx','xls','xlsx')` lowercase. Nếu BE strict → reject .DOCX. KHẢ NĂNG BUG vì FE/BE inconsistent.
- **TC-BM-417 (P0 Critical)**: A3 thiếu XSS cho rich-text editor. `mo_ta_cong_khai` render trên DN-facing site → critical XSS vector.
- **TC-BM-418**: A3 cover Switch ON với ảnh, thiếu case không upload — verify default ảnh hệ thống (srs-fr-09:304, 766).
- **TC-BM-419 (P0)**: A3 TC-BM-406 test xóa NHAP, thiếu case xóa CONG_KHAI có cascade API gỡ Cổng (EC-04 srs-fr-09:386).

### EC-05: File 05 (Tìm kiếm biểu mẫu) — 2 case

- **TC-BM-507**: Cột Mã BM (srs-fr-09:632), A3 không test exact match vs LIKE substring.
- **TC-BM-508**: INF-BM-TK-01 trên TC-BM-504 chỉ test keyword empty, thiếu filter combo empty.

### EC-06: File 06 (Import hàng loạt) — 3 case

- **TC-BM-608**: SRS srs-fr-09:663 yêu cầu Excel metadata + multi-file content; A3 không test mismatch (SPEC-CLARIFY-BM-14).
- **TC-BM-609**: SRS không quote rule duplicate filename — SPEC-CLARIFY-BM-12.
- **TC-BM-610**: A3 chỉ test multi-file boundary (TC-BM-604/605), thiếu Excel metadata 5MB boundary (srs-fr-09:663).

### EC-07: File 07 (Permission matrix) — 2 case

- **TC-BM-PERM-007**: A3 chỉ test cross-cấp TW vs BN (TC-BM-PERM-003), thiếu ngang cấp BN_A vs BN_B.
- **TC-BM-PERM-008**: A3 TC-BM-PERM-006 chỉ test DN không vào app (negative), thiếu happy path DN download qua Cổng PLQG.

---

## 3. Cross-cutting BR-EC chưa cover (đã giải quyết)

| BR-EC | Đã cover ở TC nào |
|-------|-------------------|
| BR-EC-04 storage quota 90% cảnh báo | TC-BM-606 cover 100% reject; 90% warning chưa có TC riêng — defer Phase B nếu cần |
| BR-EC-05 session limit 3 đồng thời | Cross-cutting QTHT — không cần module này |
| BR-EC-08 logout/lock blacklist | Cross-cutting QTHT |
| BR-EC-19 batch max 100/request | TC-BM-307 (publish 105) đã cover boundary |
| BR-EC-20 transactional consistency | TC-BM-305 + TC-BM-309 (timeout) + TC-BM-419 (cascade delete) |

---

## 4. Verification — count khớp với file UC sau merge

| File UC | Pre-merge | Post-merge | Δ |
|---------|----------:|-----------:|--:|
| 01-TC-quan-ly-thu-muc.md | 12 | 16 | +4 ✅ |
| 02-TC-tim-kiem-thu-muc.md | 7 | 10 | +3 ✅ |
| 03-TC-cong-khai-thu-muc.md | 7 | 9 | +2 ✅ |
| 04-TC-quan-ly-bieu-mau.md | 17 (incl. UI) | 22 | +5 ✅ |
| 05-TC-tim-kiem-bieu-mau.md | 6 | 8 | +2 ✅ |
| 06-TC-import-hang-loat.md | 8 | 11 | +3 ✅ |
| 07-TC-permission-matrix.md | 6 | 8 | +2 ✅ |
| **Total UC files** | **63** | **84** | **+21** ✅ |

**Verify command**: `grep -c "^| TC-" {file.md}` cho từng file → khớp count footer.

---

## 5. SPEC-CLARIFY mới phát sinh từ A4 merge

- **SPEC-CLARIFY-BM-11**: Whitespace trim cho ten_thu_muc (TC-TM-023)
- **SPEC-CLARIFY-BM-12**: Duplicate file names trong batch import (TC-BM-609)
- **SPEC-CLARIFY-BM-13**: Timeout policy interval cho API Cổng PLQG (TC-BM-309 — phát sinh từ A4 merge)
- **SPEC-CLARIFY-BM-14**: Excel metadata mismatch behavior (TC-BM-608)

→ Tổng SPEC-CLARIFY pending BA: 14 (BM-01..14). Sẽ gửi BA ở Phase B B-Verify.

---

## Phase B B-block ref (verified)

todo.md §W2.3 B-block list 7 file UC:
```
| B1 | 01-TC-quan-ly-thu-muc.md       | 16 |
| B2 | 02-TC-tim-kiem-thu-muc.md      | 10 |
| B3 | 03-TC-cong-khai-thu-muc.md     |  9 |
| B4 | 04-TC-quan-ly-bieu-mau.md      | 22 |
| B5 | 05-TC-tim-kiem-bieu-mau.md     |  8 |
| B6 | 06-TC-import-hang-loat.md      | 11 |
| B7 | 07-TC-permission-matrix.md     |  8 |
| TOTAL                              | 84 |
```

→ 84 TC chính, KHÔNG miss case nào. File 08 này = audit log only.

---

*Generated 2026-05-06 by BMAD A4 (edge-case-hunter) → MERGED 2026-05-06 (per plan.md §3.1 forced inline merge rule, lesson learned W2.3 BM)*
