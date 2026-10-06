# A4 — Edge Case Hunter Audit Log (FR-VIII-14..17 + FR-VIII-26)

> **Tác nhân**: bmad-review-edge-case-hunter
> **Ngày**: 2026-05-08
> **Iron rule**: TC mới → INLINE MERGE vào file UC tương ứng (`01-TC-vai-tro.md`, `02-TC-tai-khoan.md`, `03-TC-phan-quyen-du-lieu.md`, `04-TC-phan-quyen-chuc-nang.md`, `05-TC-quen-mk-kich-hoat.md`, `06-TC-permission-matrix.md`). File này là audit log (proposal + reasoning + merge mapping), KHÔNG phải TC source.

---

## 1. Edge Case Categories Hunted

| # | Category | Trigger | Đã merge file nào? |
|---|----------|---------|-------------------|
| EC-CAT-01 | **Boundary value (BVA)** — username 4-50, password ≥8, CCCD 12, mã 50, 90 ngày, 30 phút | All UC | 01 (TC-124, 127, 135-136), 02 (TC-156-159, 167, 192-193), 04, 05 (TC-127, 141) |
| EC-CAT-02 | **Unique constraint cross is_deleted** — soft delete vs unique key | UC112, UC113 | 01 (TC-128), 02 (TC-170) |
| EC-CAT-03 | **Concurrent edit / Race condition** — 2 QTHT cùng sửa | UC112, UC113 | 01 (TC-133), 02 (TC-187) |
| EC-CAT-04 | **SQL injection / XSS sanitize** — BR-EC-13 | All UC + form input | 01 (TC-125-126), 02 (TC-182-183), 05 (TC-146) |
| EC-CAT-05 | **IDOR direct API call** — non-QTHT POST/PUT/DELETE | All 4 UC112-115 | 01 (TC-132), 02 (TC-184), 03 (TC-130), 04 (TC-130), 06 (TC-020-025) |
| EC-CAT-06 | **Audit log JSON diff verify** — BR-DATA-05 cross-module | All UC | 01 (TC-130-131), 02 (TC-185-186), 03 (TC-136), 04 (TC-105, 136), 05 (TC-148), 06 (TC-050-051) |
| EC-CAT-07 | **Cache invalidation / Session refresh** — sau đổi quyền | UC114, UC115 | 03 (TC-131), 04 (TC-131) |
| EC-CAT-08 | **Cross-module trigger (SM cascade)** — FR-VIII-26 trigger SM-TVV / SM-NHT | UC tài khoản + Quên MK | 02 (TC-134), 05 (TC-102, 103, 142, 143) |
| EC-CAT-09 | **Cây 2-tầng v3.1 BR-AUTH-02** — BN/ĐP ngang cấp song song | UC114 | 03 (TC-102, TC-104-105 cha-con) |
| EC-CAT-10 | **Ngang cấp violation BR-AUTH-03** — ERR-PQ-01 | UC114 | 03 (TC-120-122) |
| EC-CAT-11 | **Token lifecycle** — vĩnh viễn vs 30 phút, expired, reused, cross-account | FR-VIII-26 | 05 (TC-123, 124, 129, 140-141, 145, 150) |
| EC-CAT-12 | **Permission cascade tree** — cha → con cascade trong UC114/UC115 | UC114, UC115 | 03 (TC-104, TC-132 cascade), 04 (TC-103-104, TC-123 inconsistent) |
| EC-CAT-13 | **Email enumerate protection** — ERR-PWD-01 trung tính | FR-VIII-26 | 05 (TC-120) |
| EC-CAT-14 | **Performance** — large selection (84 đơn vị), 50K log, 96 quyền matrix | UC114, UC115 + sibling NK | 03 (TC-134), 04 (TC-138) |
| EC-CAT-15 | **Empty state** — vai trò chưa quyền, đơn vị TAM_DUNG | UC114, UC115 | 03 (TC-137-138), 04 (TC-122) |

**Tổng edge case proposed**: ~50
**Tổng đã merge inline**: 49 (1 không merge — verify ở Phase B implementation)

---

## 2. Proposal Detail + Merge Mapping

### EC-01 — UC112 Vai trò boundary

| Proposal ID | Mô tả edge case | Reasoning | Merged vào TC |
|-------------|-----------------|-----------|---------------|
| EC-VT-01 | Mã vai trò boundary 60 ký tự (SRS không cap explicit) | BVA classic. Sibling W1.1 TC-NK-132 200 chars boundary tương tự. | 01-TC-vai-tro.md TC-124 |
| EC-VT-02 | Mã unique case-insensitive vs case-sensitive ("qtht" vs "QTHT") | DB collation default Postgres = case-sensitive nhưng app layer thường case-insensitive cho enum. SRS không nói. | 01 TC-127 |
| EC-VT-03 | Mã trùng record đã soft delete | BR-DATA-01 soft delete. Nếu unique constraint không filter is_deleted → reject; nếu có filter → resurrect. SRS không nói. | 01 TC-128 |
| EC-VT-04 | Mã chứa Unicode/dấu | SRS không restrict charset. Sibling pattern username UC113 ERR-TK-04 đã restrict ascii — vai trò có giống không? | 01 TC-135 |
| EC-VT-05 | Mô tả 5K ký tự | TEXT field unlimited DB nhưng UI có thể truncate. | 01 TC-136 |
| EC-VT-06 | Race condition 2 QTHT cùng sửa | Optimistic locking optional. | 01 TC-133 |
| EC-VT-07 | trang_thai default true vs false ngay từ đầu | SRS srs-fr-10:617 default 1 nhưng cho phép user nhập. | 01 TC-134 |

### EC-02 — UC113 Tài khoản boundary + lifecycle

| Proposal ID | Mô tả edge case | Reasoning | Merged vào TC |
|-------------|-----------------|-----------|---------------|
| EC-TK-01 | Username 3 / 4 / 50 / 51 ký tự (4 boundary) | SRS srs-fr-10:1939 "4-50 ký tự" — BVA classic. | 02 TC-156-159 |
| EC-TK-02 | Password 8 ký tự đủ 4 nhóm — VALID | SRS srs-fr-10:719 "≥ 8 ký tự + 4 nhóm" — verify lower bound. | 02 TC-154 |
| EC-TK-03 | CCCD 11 vs 12 chữ số | SRS srs-fr-10:1560 "12 chữ số" — boundary. | 02 TC-166-167 |
| EC-TK-04 | CCCD bỏ trống — optional accept | SRS srs-fr-10:1560 "Không bắt buộc". | 02 TC-168 |
| EC-TK-05 | MK = username (security weak) | Best practice security thường restrict. SRS không nói. | 02 TC-169 |
| EC-TK-06 | Email trùng email TK đã soft-delete | Cross-ref EC-VT-03 pattern. | 02 TC-170 |
| EC-TK-07 | QTHT cross-tenant tạo TK đơn vị BN khác | BR-AUTH-08 ngoại lệ cho QTHT. | 02 TC-180 |
| EC-TK-08 | Cố đặt vneid_subject cho CB nội bộ | BR-AUTH-09 chặn. | 02 TC-181 |
| EC-TK-09 | Race condition 2 QTHT phê duyệt 1 TK CHO_PHAN_QUYEN | Optimistic locking. | 02 TC-187 |
| EC-TK-10 | Batch action phê duyệt 3 TK cùng lúc (SCR-VIII-08a #5) | UI affordance. | 02 TC-188 |
| EC-TK-11 | Từ chối phê duyệt với lý do < 10 ký tự | SRS srs-fr-10:1785 "Lý do >= 10 ký tự". | 02 TC-190 |
| EC-TK-12 | Cố mở khóa TK đang HOAT_DONG (SM invalid transition) | SM guard verify. | 02 TC-191 |
| EC-TK-13 | Pagination size=200 vượt max 100 (BR-DATA-07) | Boundary. | 02 TC-193 |

### EC-03 — UC114 Phân quyền dữ liệu

| Proposal ID | Mô tả edge case | Reasoning | Merged vào TC |
|-------------|-----------------|-----------|---------------|
| EC-PQDL-01 | Cây render đúng v3.1 2-tầng (TW + BN/ĐP ngang cấp) | BR-AUTH-02 v3.1. Sibling Cấu hình HT W1.2 cũng dùng cây 2-tầng. | 03 TC-102 |
| EC-PQDL-02 | Tick TW cha → cascade 84 node | BR-AUTH-04 cha thấy con. | 03 TC-104, TC-132 |
| EC-PQDL-03 | Ngang cấp BN → DP cùng vai trò | BR-AUTH-03 ngang cấp KHÔNG thấy nhau. ERR-PQ-01. | 03 TC-120-122 |
| EC-PQDL-04 | Vai trò bị xóa giữa lúc đang phân quyền | Edge concurrent. | 03 TC-125 |
| EC-PQDL-05 | Đơn vị ID inject 99999 | IDOR test. | 03 TC-126 |
| EC-PQDL-06 | Cache invalidation sau đổi quyền | BR-AUTH-08 update cache. SPEC-CLARIFY-TKPQ-21. | 03 TC-131 |
| EC-PQDL-07 | Vai trò cap=ALL có chịu BR-AUTH-03 không (1 BN + 1 DP) | SPEC-CLARIFY-TKPQ-22. | 03 TC-133 |
| EC-PQDL-08 | Performance tick 84 node submit | Large transaction. | 03 TC-134 |
| EC-PQDL-09 | Đơn vị TAM_DUNG có hiển trong cây không | DON_VI.trang_thai filter. SPEC-CLARIFY-TKPQ-24. | 03 TC-138 |

### EC-04 — UC115 Phân quyền chức năng

| Proposal ID | Mô tả edge case | Reasoning | Merged vào TC |
|-------------|-----------------|-----------|---------------|
| EC-PQCN-01 | Cha → con cascade 6 cột × 16 module | Quy tắc tương tác srs-fr-10:1586. | 04 TC-103-104 |
| EC-PQCN-02 | Inconsistent state cha tick mà con không tick | Edge state. SPEC-CLARIFY-TKPQ-26. | 04 TC-123 |
| EC-PQCN-03 | Cache invalidation cross-FR | Sibling EC-PQDL-06. | 04 TC-131 |
| EC-PQCN-04 | Cross-module verify quyền Phê duyệt → button hiện | Quyền cột Phê duyệt. | 04 TC-132 |
| EC-PQCN-05 | Cross-module verify quyền Xuất | Quyền cột Xuất. | 04 TC-133 |
| EC-PQCN-06 | Cross-module verify quyền Xóa | Quyền cột Xóa. | 04 TC-134 |
| EC-PQCN-07 | Performance 96 quyền (16×6) tick toàn bộ | Large batch insert. | 04 TC-138 |

### EC-05 — FR-VIII-26 Quên MK

| Proposal ID | Mô tả edge case | Reasoning | Merged vào TC |
|-------------|-----------------|-----------|---------------|
| EC-PWD-01 | Email enumerate protection | ERR-PWD-01 thông báo trung tính (security best practice). | 05 TC-120 |
| EC-PWD-02 | Token vĩnh viễn cho CHO_KICH_HOAT — chờ 31 phút vẫn dùng | SRS srs-fr-10:1273 đặc biệt. | 05 TC-140 |
| EC-PWD-03 | Token 30 phút HOAT_DONG boundary | BVA. | 05 TC-141 |
| EC-PWD-04 | Token random fake không có trong DB | IDOR/security. | 05 TC-129 |
| EC-PWD-05 | Token cross-account inject user_id khác | IDOR security. | 05 TC-145 |
| EC-PWD-06 | Trigger SM-TVV side-effect verify | SRS srs-fr-10:1282 trigger entity. | 05 TC-142 |
| EC-PWD-07 | Trigger SM-NHT side-effect verify | Tương tự EC-PWD-06. | 05 TC-143 |
| EC-PWD-08 | Rate limit spam 10 request | SPEC-CLARIFY-TKPQ-08. | 05 TC-144 |
| EC-PWD-09 | XSS email payload | BR-EC-13. | 05 TC-146 |
| EC-PWD-10 | User HOAT_DONG đã login click "Quên MK" | Edge state. SPEC-CLARIFY-TKPQ-28. | 05 TC-147 |
| EC-PWD-11 | Audit log PASSWORD_RESET / ACCOUNT_ACTIVATE actions | BR-DATA-05. | 05 TC-148 |

### EC-06 — Cross-FR Permission Matrix

| Proposal ID | Mô tả edge case | Reasoning | Merged vào TC |
|-------------|-----------------|-----------|---------------|
| EC-PERM-01 | IDOR trên 4 UC × 4 method (POST/PUT/PATCH/DELETE) | BR-AUTH-01 cross-FR. | 06 TC-020-025 |
| EC-PERM-02 | QTHT cross-tenant bypass BR-AUTH-08 | Verify ngoại lệ. | 06 TC-005, TC-040, TC-041 |
| EC-PERM-03 | Audit log cross-FR | BR-DATA-05. | 06 TC-050-051 |

---

## 3. Edge case proposed nhưng KHÔNG merge

| Proposal ID | Mô tả | Reasoning từ chối |
|-------------|-------|-------------------|
| EC-DEFER-01 | Stress test 10K vai trò + 50K TK list rendering | Volume `~100-2000 records` (srs-fr-10:1954, 1991) — không phải scale cao. Defer Phase B nếu cần. |

---

## 4. Tổng kết A4

| Metric | Value |
|--------|-------|
| Edge case proposed | 50 |
| Inline merged vào file UC | 49 |
| Defer Phase B | 1 |
| File UC bị thay đổi | 6 (01-06) |

**Lesson learned applied (W2.3 Biểu mẫu pattern):** Mọi TC mới đã Edit trực tiếp vào file UC — KHÔNG sống ở file 08 này. File 08 chỉ là audit log.

---

## 5. Verify count

```
grep unique TC IDs:
01-TC-vai-tro.md          → 29 TC
02-TC-tai-khoan.md        → 66 TC (boundary tách 4 con cho username 3/4/50/51 + CCCD 11/12)
03-TC-phan-quyen-du-lieu.md → 24 TC
04-TC-phan-quyen-chuc-nang.md → 21 TC
05-TC-quen-mk-kich-hoat.md → 28 TC
06-TC-permission-matrix.md → 27 TC
                            ─────
Tổng                       → 195 TC
```

> **vs estimate todo.md ~178**: +17 TC do cover hết SRS BR/AC/SM/SM-TAIKHOAN 12 transitions + 19 ERR codes + 16 AC + edge case + permission matrix cross-FR (user yêu cầu cover hết SRS, không cap cứng 178).

---

## 3. Phụ lục — UC120 FR-VIII-22 (NEW append 2026-05-10)

> **File mới**: `12-TC-self-registration-dn.md`. A4 audit này append vì UC120 mới được mở rộng scope W1.4 ngày 2026-05-10. KHÔNG sửa các edge case proposal cũ ở Section 1-2.

### EC-08 — UC120 Self-registration DN edge cases

| Proposal ID | Mô tả edge case | Reasoning | Merged vào TC |
|-------------|-----------------|-----------|---------------|
| EC-REG-01 | Unicode tên DN — VN diacritics + CJK ký tự | DOANH_NGHIEP entity không restrict charset. UTF-8 default. Sibling EC-VT-04 vai trò Unicode pattern. | 12-TC TC-REG-200 |
| EC-REG-02 | Whitespace trim leading/trailing tự động | Data quality edge — common trap khi user copy-paste. Không nêu explicit trong SRS. | 12-TC TC-REG-201 |
| EC-REG-03 | MST `0123456789` leading zero preserve (KHÔNG cast int) | Nếu BE store int → mất `0` → bug critical (sai khóa định danh DN). Edge ưu tiên P0. | 12-TC TC-REG-202 |
| EC-REG-04 | SĐT international `+84...` format | SRS không nêu regex SĐT cụ thể. Common edge khi DN nước ngoài. | 12-TC TC-REG-203 |
| EC-REG-05 | File upload duplicate name | Storage path collision. BE phải auto-rename / append UUID. | 12-TC TC-REG-204 |
| EC-REG-06 | MIME type spoof — `.exe` rename `.pdf` | Security edge — magic byte check vs extension check. P0 nếu BE không magic-byte verify → upload payload bug. | 12-TC TC-REG-205 |
| EC-REG-07 | Re-register với MST của DN đã soft-deleted | BR-DATA-01 soft delete + BR-DATA-02 unique. Cross-ref EC-VT-03 + EC-TK-06 pattern. SRS không nói có filter is_deleted khi check unique không. | 12-TC TC-REG-206 |
| EC-REG-08 | Re-register với email TK đã VO_HIEU_HOA | TAI_KHOAN VHH vẫn lock email? Cross-ref EC-REG-07 pattern. | 12-TC TC-REG-207 |
| EC-REG-09 | Tên DN trùng (ten_doanh_nghiep KHÔNG unique theo spec) | SRS chỉ unique MST/email/username. Tên DN có thể trùng — verify spec đúng. | 12-TC TC-REG-208 |
| EC-REG-10 | Network failure mid-submit (BE commit / FE timeout) | Idempotent test. Common bug khi user retry sau timeout → duplicate record. | 12-TC TC-REG-209 |
| EC-REG-11 | Browser autofill password vs strength indicator | UX edge. Password indicator phải react với autofill event (không chỉ keystroke). | 12-TC TC-REG-210 |
| EC-REG-12 | Email IDN (Unicode local-part / domain) — RFC 6531 vs 5322 | SRS chỉ ghi RFC 5322 → KHÔNG support IDN. Verify spec strict hay loose. | 12-TC TC-REG-211 |
| EC-REG-13 | Cancel button cleanup file uploaded tạm | Storage leak nếu BE không cleanup. Defer Phase B verify storage trực tiếp. | 12-TC TC-REG-212 |

### Categories cập nhật (SECTION 1 cumulative)

UC120 đóng góp các category mới + reuse 5 category cũ:

| Category | Đã merge file nào? (cumulative) |
|----------|--------------------------------|
| EC-CAT-01 BVA | 01, 02, 04, 05, **12 (TC-REG-115..118 MST, 137 email RFC, 151..154 username 4/3/50/51, 157..158 password 7/8)** |
| EC-CAT-02 Soft-delete unique | 01 TC-128, 02 TC-170, **12 TC-REG-206 MST + 207 email** |
| EC-CAT-03 Race condition | 01, 02, **12 TC-REG-198 double submit + 199 concurrent MST + 209 network mid-submit** |
| EC-CAT-04 SQL/XSS sanitize BR-EC-13 | 01, 02, 05, **12 TC-REG-113 ten XSS** |
| EC-CAT-05 IDOR direct API | 01, 02, 03, 04, 06, 07 IDOR suite (UC120 public — không có IDOR concept) |
| EC-CAT-06 AUDIT_LOG | 01, 02, 03, 04, 05, 06, **12 TC-REG-190 SELF_REGISTER_DN** |
| EC-CAT-13 Email enumerate | 05 TC-120, **12 — KHÔNG áp dụng (UC120 register, không reset; email trùng = ERR-REG-02 explicit theo spec)** |
| **EC-CAT-16 (NEW) Unicode + i18n** | **12 TC-REG-200 ten CJK + 211 email IDN** |
| **EC-CAT-17 (NEW) Data integrity (whitespace, leading-zero, MIME spoof)** | **12 TC-REG-201, 202, 205** |
| **EC-CAT-18 (NEW) File upload edge** | **12 TC-REG-204 dup name + 205 MIME spoof + 212 cancel cleanup** |
| **EC-CAT-19 (NEW) Public access edge (no auth)** | **12 TC-REG-192 direct URL + 193/194 CB submit edge** |
| **EC-CAT-20 (NEW) UX state (browser autofill, indicator)** | **12 TC-REG-210** |

### Thống kê count UC120

```
12-TC-self-registration-dn.md → 64 TC (51 base A3 + 13 edge A4)
                                  Section A Happy: 6
                                  Section B Validation Nhóm 1: 23
                                  Section C Validation Nhóm 2: 18
                                  Section D ERR-REG: 6
                                  Section E Security/Audit/Integration: 10
                                  Section F Edge (A4 merged): 13
```

**Tổng cumulative W1.4 sau UC120**: 195 + 64 = **259 TC** (184 functional gốc + 16 security + **64 UC120 functional NEW**) — sẽ adjust thêm sau A6 fill + A7 filter.
