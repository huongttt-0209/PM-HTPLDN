# A6 — Test Quality Review (DM Dùng Chung)

> **Date:** 2026-05-08
> **Reviewer:** BMAD test-arch-test-review
> **Scope:** 10 file UC test (file 01..10) + 3 gap fill từ A5 → INLINE MERGE

---

## 1. Test Quality Score

### 1.1 Per-file score

| File | TC count | Coverage BR | Coverage AC | Coverage Error | Edge case depth | Quality |
|------|----------|-------------|-------------|----------------|-----------------|---------|
| 01-TPL-DM-CRUD (LV PL) | 58 | 100% chính + cross | 100% | 100% | High (8 edge) | 9.5/10 |
| 02-Smoke-11-DM | 55 | TPL pattern verify | 100% basic | 80% | Low (smoke only) | 8.5/10 |
| 03-Cơ quan ĐV tree | 35 | BR-AUTH-02 100% + BR-DATA 100% | 100% | 100% (5 ERR-DV) | High (3 edge tree-specific) | 9.3/10 |
| 04-Tiêu chí HQ | 20 | BR-CALC-04 100% | 100% | 100% (ERR-TC-01 + WRN-TC-01) | Mid (2 edge) | 9.0/10 |
| 05-Tiêu chí CP | 17 | TPL pattern | 100% | 80% (relies TPL ERR-DM) | Mid (2 edge) | 8.8/10 |
| 06-Chương trình HT | 11 | TPL + date | 100% | 80% | Mid (1 edge snapshot) | 8.5/10 |
| 07-Tình trạng VV | 11 | TPL + thu_tu Y + màu | 100% | 100% | Mid (1 edge cascade msg) | 8.7/10 |
| 08-Loại DN | 10 | TPL + 2 fields | 100% | 80% | Low | 8.5/10 |
| 09-Hồ sơ thành phần | 16 | TPL + JSON | 100% | 80% | Mid (1 edge dup) | 8.7/10 |
| 10-Permission matrix | 16 | BR-AUTH-01 cross 100% | 100% | 100% | High (16 explicit) | 9.5/10 |

**Avg quality:** 8.9/10

### 1.2 Overall metrics

- **Total TC active:** **255** (final sau A1-A7 + R1/R2/R3 Codex review)
  - A3 base: 228 (47+55+32+18+15+10+10+10+15+16)
  - A4 edge inline: +18 → 246
  - A6 gap fill: +3 → 249
  - R2 Codex fill: +9 (UC103 ×3, UC109 ×4, UC110 ×2) → 258 declared
  - R3 Codex LOẠI: −3 (TC-LV-036/-044, TC-PERM-008) → **255 active**
  - R3 Codex REPHRASE: 7 TC (assumption/DB direct → UI bridge)
  - File-level active: 56+55+38+24+19+11+11+10+16+15 = **255** ✅
- **BR coverage:** 100% explicit (sau A6 fill 3 GAP)
- **AC coverage:** 100%
- **Error code coverage:** 14/14 = 100%
- **Permission matrix:** 5/5 role × CRUD = 100%
- **SPEC-CLARIFY listed:** 26 entries (gửi BA Phase B)

---

## 2. Issues found

| # | Issue | Severity | Action | Status |
|---|-------|----------|--------|--------|
| I1 | File 02 smoke 11 DM × 5 = 55 TC nhưng coverage chỉ basic (List+Create+Validate+Update+Delete) — KHÔNG cover edge | Low | Acceptable — smoke pattern intentional; deep test ở file UC riêng | ✅ OK |
| I2 | TC-LDN-001..005 ID conflict giữa file 02 (smoke Loại DN) và file 08 (deep Loại DN) | Low | Đổi prefix file 08 → TC-LDN-DEEP-001..010 | ✅ resolved ở A7 — file 08 đã dùng `TC-LDN-DEEP-001..010` (verify bằng `grep -c "TC-LDN-DEEP-" 08-TC-loai-dn-tieu-chi.md` = 10) |
| I3 | BR-AUTH-08 partial coverage trước A6 fill | Medium | Filled qua TC-LV-FILL-001 | ✅ resolved |
| I4 | BR-DATA-02 + BR-DATA-03 partial trước A6 fill | Medium | Filled qua TC-LV-FILL-002, FILL-003 | ✅ resolved |
| I5 | BR-DATA-06 (Export Excel max 10K) — SCR-VIII-01 KHÔNG có nút Export | N/A | KHÔNG TC — ghi note `[SPEC-CLARIFY-DM-27]` cho BA xác nhận có/không có Export | 📝 logged |
| I6 | BR-AUTH-03 (ngang cấp KHÔNG thấy nhau) — cross-FR, test ở module dùng | N/A | KHÔNG nằm trong scope DM W1.3 | ✅ OK |
| I7 | Edge case "Tab switching with unsaved changes (modal warning)" — chưa có TC | Low | Acceptable — UX detail, có thể add ở Phase B nếu cần | ✅ OK (defer) |

---

## 3. Inline merge summary

**TC mới thêm sau A4 + A6:**
- A4 edge: 18 TC (TC-LV-EDGE-001..008, TC-CQDV-EDGE-001..003, TC-TCHQ-EDGE-001..002, TC-TCCP-EDGE-001..002, TC-CT-EDGE-001, TC-TT-EDGE-001, TC-HS-EDGE-001)
- A6 fill: 3 TC (TC-LV-FILL-001..003)

**TC delta:** 228 (A3 base) → 246 (A4) → 249 (A6) → 258 (R2 fill) → **255 active (R3 LOẠI 3)** = file footer active sum 56+55+38+24+19+11+11+10+16+15 ✅

---

## 4. Action item cho A7 — DONE

- I2: ✅ Đổi ID prefix file 08 từ `TC-LDN-XXX` → `TC-LDN-DEEP-XXX` đã thực hiện ở A7 (replace_all 10 occurrences)

---

## 5. SPEC-CLARIFY tổng hợp (gửi BA Phase B)

| ID | Vấn đề | File phát hiện |
|----|---------|---------------|
| SPEC-CLARIFY-DM-01 | Empty state text exact | 00 + 01 |
| SPEC-CLARIFY-DM-02 | FR-VIII-06 Tổ chức tư vấn ẩn UI? | 00 |
| ~~SPEC-CLARIFY-DM-03~~ | ~~UC102 thu_tu Y bắt buộc vs TPL N~~ — **CLEARED R4** (line 277 nguyên văn Y) | — |
| SPEC-CLARIFY-DM-04 | UC101 thoi_gian_ket_thuc < bat_dau | 00 + 06 |
| ~~SPEC-CLARIFY-DM-05~~ | ~~UC109 trong_so range~~ — **CLEARED R4** (line 532 "0-100%" rõ) | — |
| SPEC-CLARIFY-DM-06 | UC109 thang_diem_max upper bound | 00 + 04 |
| ~~SPEC-CLARIFY-DM-07~~ | ~~BR-CALC-04 trọng số > 100% cap upper~~ — **CLEARED R4** (WARNING không cap) | — |
| SPEC-CLARIFY-DM-08 | UC110 muc_ho_tro_phan_tram boundary | 00 + 05 |
| SPEC-CLARIFY-DM-09 | UC110 tran_ho_tro_nam negative | 00 + 05 |
| ~~SPEC-CLARIFY-DM-10~~ | ~~UC103 TW có cha~~ — **CLEARED R4** (line 1967 NULL khi cap=TW rõ) | — |
| SPEC-CLARIFY-DM-11 | UC103 đổi cap với children | 00 + 03 |
| SPEC-CLARIFY-DM-12 | UC106/107 thanh_phan JSON shape | 00 + 09 |
| SPEC-CLARIFY-DM-13 | Mã DM ký tự đặc biệt cho phép | 00 + 01 |
| ~~SPEC-CLARIFY-DM-14~~ | ~~Pagination per-tab cap~~ — **CLEARED R4** (BR-DATA-07 max 100 rõ) | — |
| ~~SPEC-CLARIFY-DM-15~~ | ~~UC103 nút [+ Thêm con] cho BN/DP~~ — **CLEARED R4** (BR-AUTH-02 2-tier rõ) | — |
| ~~SPEC-CLARIFY-DM-16~~ | ~~UC103 cap=DP với cha=BN~~ — **CLEARED R4** (line 319 "cha phải = TW") | — |
| ~~SPEC-CLARIFY-DM-17~~ | ~~Multi-TW cho phép?~~ — **CLEARED R4** (BR-AUTH-02 1 TW root rõ) | — |
| SPEC-CLARIFY-DM-18 | Xóa TW root guard? | 03 |
| SPEC-CLARIFY-DM-19 | UC105 max length text tiêu chí | 08 |
| SPEC-CLARIFY-DM-20 | Whitespace handling ma + ten | 01 |
| SPEC-CLARIFY-DM-21 | Soft-deleted + re-create cùng ma | 01 |
| SPEC-CLARIFY-DM-22 | UC103 đổi cap TW → BN/DP có children | 03 |
| SPEC-CLARIFY-DM-23 | UC103 trang_thai TAM_DUNG impact session active | 03 |
| SPEC-CLARIFY-DM-24 | UC110 muc_ho_tro decimal | 05 |
| SPEC-CLARIFY-DM-25 | UC101 snapshot pattern khi sửa thoi_gian | 06 |
| SPEC-CLARIFY-DM-26 | UC106/107 thành phần item duplicate ten | 09 |
| ~~SPEC-CLARIFY-DM-27~~ | ~~BR-DATA-06 Export Excel có UI button không?~~ — **CLEARED R4** (out-of-scope SCR-VIII-01) | — |

**Total SPEC-CLARIFY:** 29 entries → **20 entries active sau R4 cleanup** (9 cleared: DM-03/05/07/10/14/15/16/17/27 — verified SRS rõ ngay từ spec)

---

## 6. Phase A done acceptance

- ✅ A1-A6 done
- ✅ Traceability ≥95% BR (sau A6 = 100%)
- ✅ AC 100%
- ✅ Error code 100%
- ✅ Permission matrix 100%
- ✅ Inline merge rule complied (18 edge + 3 fill all merged vào file UC)
- 🔵 A7 pending — 1 action item (đổi ID prefix file 08)
