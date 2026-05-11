# Functional Test Report — Chi trả full flow (R3 verify dev fix)

> **Module:** Chi trả chi phí (FR-06 / FR-V.II) · **Round:** R7-R3 (2026-05-10) · **Tester:** QA Automation via Claude Code (Chrome DevTools MCP)
> **SRS:** [`srs-update-2026-5-5/srs-fr-06-chi-tra.md`](../../../../input/srs-update-2026-5-5/srs-fr-06-chi-tra.md) · [`02-thu-tu-module.md §10 SM-CHI-TRA v3.5`](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)
> **Bug:** [`Pass-bug-report-flow-chi-tra.md`](../../bug-reports/chi-tra/Pass-bug-report-flow-chi-tra.md) — 7/7 đóng
> **Pool seed verify:** [`verify-checklist-r7-e3-chi-tra-100-hsct.md`](../../seed/chi-tra/verify-checklist-r7-e3-chi-tra-100-hsct.md) — 40/40 BR-OK

---

## Kết luận

✅ **PASS** — 11/12 TC executed PASS, 1/12 BLOCKED do DN-only path (đúng spec). TC-FULL-12 BR-AUTH-05 verified PASS sau khi login cb_nv_dp_02 (BG).

| TC | Phạm vi | Kết quả | Bằng chứng |
|---|---|---|---|
| TC-FULL-01 | B2 CTN→DKT (Tiếp nhận) | ✅ PASS | HSCT200002 lịch sử "Tiếp nhận → Đang kiểm tra" 10/05 20:57 |
| TC-FULL-02 | B3 DKT→DDG (Đạt) | ✅ PASS | HSCT200003 walk happy path |
| TC-FULL-03 | B4 DKT→YCBS (Yêu cầu bổ sung) | ✅ PASS | [r3-tc-full-03-b4-dkt-ycbs-PASS.png](image/r3-tc-full-03-b4-dkt-ycbs-PASS.png) |
| TC-FULL-04 | B5 YCBS→DKT (DN bổ sung) | 🚫 BLOCKED | DN-only path; HSCT200002 YCBS không render Kiểm tra form ở CB UI (đúng spec — chờ DN upload). Giống R7.7.12.2. |
| TC-FULL-05 | B6 DDG→DTD (Trình thẩm định) | ✅ PASS | HSCT200001/HSCT000034 walk |
| TC-FULL-06 | B7 DTD→CPD (Trình PD) | ✅ PASS | HSCT200001/HSCT000034 walk |
| TC-FULL-07 | B8 CPD→DTD (Trả về thẩm định) | ✅ PASS | [r3-bug006-after-fix-tra-ve-tham-dinh.png](../../bug-reports/chi-tra/image/r3-bug006-after-fix-tra-ve-tham-dinh.png) — endpoint + button + modal đều "Trả về thẩm định" |
| TC-FULL-08 | B9 CPD→DA_DUYET (Phê duyệt) | ✅ PASS | HSCT200003 walk |
| TC-FULL-09 | B10 DA_DUYET→DA_THANH_TOAN (Cập nhật thanh toán xác nhận) | ✅ PASS | HSCT200003 walk; form B11 render đầy đủ với cb_nv_dp_01 |
| TC-FULL-10 | B12 DA_DUYET→TU_CHOI_THANH_TOAN (Cập nhật thanh toán từ chối) | ✅ PASS | [r3-tc-full-10-b12-tuchoi-thanhtoan-PASS.png](image/r3-tc-full-10-b12-tuchoi-thanhtoan-PASS.png) — HSCT200021 trạng thái "Từ chối" 10/05 20:53 |
| TC-FULL-11 | BR-CALC-01/02 (mức HT theo size + công thức MIN) | ✅ PASS | HSCT200003 (Vừa) duyệt 6.000.000 = MIN(75.000.000, 6.000.000, ~6.074M trần) ✅ |
| TC-FULL-12 | BR-AUTH-05 (CB chỉ thấy hồ sơ cùng don_vi_id) | ✅ PASS | cb_nv_dp_02 (BG) thấy 24 hồ sơ BG-only (Phương Đông BG / Thành Đạt BG / Tân Phú BG), 0 AG record. Direct URL HSCT000001 (Bình Minh AG) trả 403 BE + UI "Không tìm thấy hồ sơ chi trả". [r3-tc-full-12-br-auth-05-bg-list-PASS.png](image/r3-tc-full-12-br-auth-05-bg-list-PASS.png) · [r3-tc-full-12-direct-url-AG-blocked-403.png](image/r3-tc-full-12-direct-url-AG-blocked-403.png) |

---

## Tài khoản dùng

| Username | Vai trò | Phạm vi | Dùng cho |
|---|---|---|---|
| `cb_nv_dp_01` | CB Nghiệp vụ ĐP | An Giang (AG) | B2-B7, B10-B12 |
| `cb_pd_dp_01` | CB Phê duyệt ĐP | An Giang (AG) | B8, B9 |
| `cb_nv_dp_02` | CB Nghiệp vụ ĐP | Bắc Giang (BG) | TC-FULL-12 BR-AUTH-05 cross-don_vi |

OTP bypass `666666` ở MailHog.

---

## Pool data

40 HSCT distribution sau dev re-seed R3 ([`verify-checklist-r7-e3-chi-tra-100-hsct.md`](../../seed/chi-tra/verify-checklist-r7-e3-chi-tra-100-hsct.md)):
- BR-CALC-01 (mức HT theo size): 40/40 đúng — SIEU_NHO=100%/3M, NHO=30%/5M, VUA=10%/10M
- BR-CALC-02 (công thức): 40/40 đúng `MIN(soTienDeNghi, floor(phiTuVan × pct/100), tranHoTroNam − daChiTrongNam)` clamp 0
- 8/8 sample detail verify trần năm khớp size

---

## State Machine SM-CHI-TRA v3.5 — 12 transitions verified

```
[CHO_TIEP_NHAN] ── B2 Tiếp nhận ──→ [DANG_KIEM_TRA]
                                          │
                  ┌── B3 Đạt ────────────→ [DANG_DANH_GIA]
                  ├── B4 YCBS ──────────→ [YEU_CAU_BO_SUNG] ─ B5 DN bổ sung ──→ (back to DKT)
                  └── B5(neg) Không đạt → [TU_CHOI]
                                          │
[DANG_DANH_GIA] ── B6 Trình TĐ ──────────→ [DANG_THAM_DINH]
                                          │
[DANG_THAM_DINH] ── B7 Trình PD ─────────→ [CHO_PHE_DUYET]
                                          │
                  ┌── B8 Trả về TĐ ──────→ [DANG_THAM_DINH]
                  └── B9 Phê duyệt ──────→ [DA_DUYET]
                                          │
[DA_DUYET] ── B10 Cập nhật TT (xác nhận) ─→ [DA_THANH_TOAN]
            └── B12 Cập nhật TT (từ chối) ─→ [TU_CHOI_THANH_TOAN]
```

11/12 transitions verified ở R3 (B5 DN-only blocked, đúng spec).

---

## Bug summary R3

7/7 bug đóng — chi tiết ở [`Pass-bug-report-flow-chi-tra.md`](../../bug-reports/chi-tra/Pass-bug-report-flow-chi-tra.md):

| BUG-ID | Severity | Title | Status R3 |
|---|---|---|---|
| BUG-CHITRA-001 | Critical | Pool 97/108 sai BR-CALC | ✅ Closed (re-seeded 40/40) |
| BUG-CHITRA-002 | Major | Form Kiểm tra thiếu trường tài liệu | ✅ Closed (18 trường render đủ) |
| BUG-CHITRA-003 | Medium | Form Kiểm tra thiếu radio "Không đạt" | ✅ Closed (3 outcome) |
| BUG-CHITRA-004 | Medium | Lịch sử lộ enum code | ✅ Closed (Vietnamese) |
| BUG-CHITRA-005 | Minor | Spinbutton soTienDuyet không bound trần | ✅ Closed |
| BUG-CHITRA-006 | Minor | B8 wording "Từ chối" thay vì "Trả về thẩm định" | ✅ Closed (3/3 layer) |
| BUG-CHITRA-007 | Minor | Form B10/B12 không render | ✅ Closed (false positive R2 — sai role) |

---

## Bằng chứng tổng hợp

- **B4 DKT→YCBS:** [r3-tc-full-03-b4-dkt-ycbs-PASS.png](image/r3-tc-full-03-b4-dkt-ycbs-PASS.png)
- **B12 DA_DUYET→TU_CHOI_THANH_TOAN:** [r3-tc-full-10-b12-tuchoi-thanhtoan-PASS.png](image/r3-tc-full-10-b12-tuchoi-thanhtoan-PASS.png)
- **B8 wording fix:** [r3-bug006-after-fix-tra-ve-tham-dinh.png](../../bug-reports/chi-tra/image/r3-bug006-after-fix-tra-ve-tham-dinh.png)
- **B11 form render correct role:** [r3-bug007-form-renders-cb-nv-dp.png](../../bug-reports/chi-tra/image/r3-bug007-form-renders-cb-nv-dp.png)
- **BR-AUTH-05 cross-don_vi list scope:** [r3-tc-full-12-br-auth-05-bg-list-PASS.png](image/r3-tc-full-12-br-auth-05-bg-list-PASS.png) — BG account thấy 24 BG hồ sơ, 0 AG
- **BR-AUTH-05 direct URL block:** [r3-tc-full-12-direct-url-AG-blocked-403.png](image/r3-tc-full-12-direct-url-AG-blocked-403.png) — API 403 + UI "Không tìm thấy hồ sơ chi trả"

---

## Module status sau R3

✅ Chi trả chi phí READY FOR PRODUCTION — 11/12 TC PASS, 7/7 bug đóng, pool 40/40 BR-OK, BR-AUTH-05 isolation enforced cả BE (403) + UI (404 wording).

Còn lại defer R4: TC-FULL-04 (B5 DN bổ sung — cần seed DN credentials hoặc dev seed HSCT cho QA DN, đang tracked ở R7.7.12.2 BLOCKED).
