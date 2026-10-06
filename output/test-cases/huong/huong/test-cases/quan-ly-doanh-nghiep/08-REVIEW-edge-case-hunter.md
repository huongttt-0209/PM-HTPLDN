# 08 — A4 Edge Case Hunter Review (audit log)

> **Skill**: bmad-review-edge-case-hunter
> **Ngày chạy**: 2026-05-09
> **Module**: FR-07 W2.1 Quản lý DN
> **Iron rule**: TC mới đã MERGE TRỰC TIẾP vào Section "E/F/G/H/I. EDGE bổ sung" của file UC tương ứng. File này CHỈ là audit log.

---

## A. Tổng kết edge cases

**Tổng đề xuất**: 37 edge case
**Tổng merge inline**: 37/37 (100%)
**Tổng LOẠI**: 0
**Tổng PARTIAL**: 0

---

## B. Phân loại theo nhóm edge

| Nhóm | Count | Loại | Files affected |
|------|---:|---|---|
| Concurrency / Race | 4 | Edit cùng DN, Race CREATE same MST, 2 user CREATE HSPL, Click VV soft-deleted | 01, 03, 04 |
| Unicode / Internationalization | 2 | Tên DN multi-language emoji + Search no-dấu accent-insensitive | 01, 02 |
| Whitespace / Trim | 1 | Leading/trailing space ten_doanh_nghiep | 01 |
| XSS sanitize | 4 | ten_doanh_nghiep XSS, tu_khoa XSS, ten_ho_so XSS, IDOR direct API | 01, 02, 03, 06 |
| SQL injection | 2 | tu_khoa, ma_so_thue | 01, 02 |
| Format MST | 1 | MST không phải 10 chữ số reject | 01 |
| Boundary string length | 1 | tu_khoa 200/201 char | 02 |
| File upload edge | 3 | 0-byte, extension spoof, file > 20MB | 01, 03 |
| Soft delete / Restore | 3 | DN soft-deleted restore, HSPL file orphan, HSCT soft-deleted | 01, 03, 05 |
| Counter sync | 3 | KPI desync detect, NULL chi_phi, soft-deleted KHÔNG đếm | 04 |
| Date logical | 3 | tu_ngay > den_ngay (search), ngay_cap > ngay_het_han (HSPL), Reversed range (search) | 02, 03 |
| Timezone UTC+7 | 1 | Boundary date filter | 02 |
| Sort secondary | 1 | Tie-breaker by id DESC | 02 |
| Performance | 2 | 1000 VV / HSCT large data | 04, 05 |
| Session / Auth | 3 | Session expire edit, OTP brute force, TAI_KHOAN.email conflict | 06 |
| MST chi nhánh 13 chữ số | 1 | Block self-reg | 06 |
| DN.email NOT UNIQUE | 1 | 100 DN cùng email | 06 |
| IDOR direct API | 1 | fetch GET cross-tenant | 06 |
| Filter scope | 1 | Tab 4 filter trang_thai HSCT | 05 |
| VV without HSCT | 1 | DN có VV nhưng VV không có HSCT | 05 |

---

## C. Merge mapping (proposal → file UC)

| Edge ID | Loại | File merge | Section |
|---------|------|------|---|
| EDGE-A4-a Concurrency Edit | High | 01-CRUD | E (TC-DN-301) |
| EDGE-A4-b Unicode tên DN | Medium | 01-CRUD | E (TC-DN-302) |
| EDGE-A4-c Whitespace trim | Medium | 01-CRUD | E (TC-DN-303) |
| EDGE-A4-d XSS ten_doanh_nghiep | High | 01-CRUD | E (TC-DN-304) |
| EDGE-A4-e SQL injection MST | High | 01-CRUD | E (TC-DN-305) |
| EDGE-A4-f MST 10 chữ số format | Medium | 01-CRUD | E (TC-DN-306) |
| EDGE-A4-g File 0-byte upload | Medium | 01-CRUD | E (TC-DN-307) |
| EDGE-A4-h Race CREATE same MST | High | 01-CRUD | E (TC-DN-308) |
| EDGE-A4-i Soft-deleted DN restore | Medium | 01-CRUD | E (TC-DN-309) |
| EDGE-A4-j SQL injection tu_khoa | High | 02-Search | G (TC-DN-TK-501) |
| EDGE-A4-k XSS in tu_khoa | High | 02-Search | G (TC-DN-TK-502) |
| EDGE-A4-l Unicode no-dấu | Medium | 02-Search | G (TC-DN-TK-503) |
| EDGE-A4-m Boundary 200 char tu_khoa | Medium | 02-Search | G (TC-DN-TK-504) |
| EDGE-A4-n Reversed date range | Medium | 02-Search | G (TC-DN-TK-505) |
| EDGE-A4-o Timezone UTC+7 boundary | Medium | 02-Search | G (TC-DN-TK-506) |
| EDGE-A4-p Sort secondary tie-breaker | Medium | 02-Search | G (TC-DN-TK-507) |
| EDGE-A4-q Concurrent CREATE HSPL | Medium | 03-HSPL | I (TC-HSPL-701) |
| EDGE-A4-r ngay_cap > ngay_het_han | Medium | 03-HSPL | I (TC-HSPL-702) |
| EDGE-A4-s DELETE HSPL có file orphan | Medium | 03-HSPL | I (TC-HSPL-703) |
| EDGE-A4-t File extension spoofing | High | 03-HSPL | I (TC-HSPL-704) |
| EDGE-A4-u ten_ho_so XSS | High | 03-HSPL | I (TC-HSPL-705) |
| EDGE-A4-v Bulk delete sequence | Medium | 03-HSPL | I (TC-HSPL-706) |
| EDGE-A4-w VV chi_phi NULL | Medium | 04-LSHT | E (TC-LS-301) |
| EDGE-A4-x Performance 1000 VV | Medium | 04-LSHT | E (TC-LS-302) |
| EDGE-A4-y VV soft-deleted KHÔNG đếm | High | 04-LSHT | E (TC-LS-303) |
| EDGE-A4-z Counter desync detect | Medium | 04-LSHT | E (TC-LS-304) |
| EDGE-A4-aa Click VV soft-deleted race | Medium | 04-LSHT | E (TC-LS-305) |
| EDGE-A4-bb HSCT soft-deleted ẩn | High | 05-HSCT | F (TC-CT-401) |
| EDGE-A4-cc Filter trang_thai HSCT | Medium | 05-HSCT | F (TC-CT-402) |
| EDGE-A4-dd Performance 1000 HSCT | Medium | 05-HSCT | F (TC-CT-403) |
| EDGE-A4-ee VV không liên kết HSCT | Medium | 05-HSCT | F (TC-CT-404) |
| EDGE-A4-ff Session expire edit | Medium | 06-Permission | H (TC-DN-PERM-601) |
| EDGE-A4-gg OTP brute force | Medium | 06-Permission | H (TC-DN-PERM-602) |
| EDGE-A4-hh TAI_KHOAN.email conflict | Medium | 06-Permission | H (TC-DN-PERM-603) |
| EDGE-A4-ii MST 13 chữ số chi nhánh | Medium | 06-Permission | H (TC-DN-PERM-604) |
| EDGE-A4-jj IDOR direct API | High | 06-Permission | H (TC-DN-PERM-605) |
| EDGE-A4-kk DN.email 100 trùng | Medium | 06-Permission | H (TC-DN-PERM-606) |

---

## D. Reasoning notes

### High priority (10/37)
- XSS + SQL injection: bắt buộc mọi text input → security baseline
- Race conditions: BR-DATA-04 SEQ atomic + UNIQUE MST → backend integrity
- Soft delete invariants: Tab 3/4 chỉ đếm active records; HSCT/HSPL is_deleted=1 ẩn → BR-DATA-01 enforce
- IDOR direct API: BR-AUTH-08 enforce trên backend không chỉ UI

### Medium priority (27/37)
- Counter sync, performance, timezone, sort secondary, file upload edge: best practice + spec gap discovery
- SPEC-CLARIFY phát sinh 14 entries (DN-23 đến DN-42) chờ BA — đã list ở 11-a7-filter-log.md (sẽ tạo)

### KHÔNG merge (0)
N/A — tất cả 37 edge đều merge inline.

---

**— Hết 08 A4 Audit FR-07 —**
