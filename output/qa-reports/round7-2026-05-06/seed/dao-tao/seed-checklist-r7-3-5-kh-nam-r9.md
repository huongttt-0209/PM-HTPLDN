# Seed Checklist — Kế hoạch Đào tạo Năm (R7.3.5 — R9 re-run)

**Ngày:** 2026-05-09 19:21–19:30 • **Tài khoản:** `cb_nv_tw_02` + `cb_nv_bn_02` + `cb_nv_dp_02` • **Trạng thái mong đợi:** `Nháp` (NHAP)
**Màn:** SCR-III-00 — Kế hoạch đào tạo năm • **Đường dẫn:** `/dao-tao/ke-hoach/danh-sach`
**SRS:** [FR-III-14 UC33 — Lập kế hoạch đào tạo năm](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-14)
**Round:** R9 — re-run sau khi 4 record cũ (R7+R8) đã advance qua R7.4.B0 verify.

---

## Downstream consumer × filter

| Task downstream | Filter | Số record cần | State | Verify | Status |
|---|---|---|---|---|:--:|
| R7.4.B0 — Workflow KH năm | `trangThai=NHAP` để Trình duyệt → CHO_DUYET | ≥1 NHAP/cấp | NHAP | `GET /ke-hoach-dao-taos?trangThai=NHAP` ≥1 mỗi cấp | ✅ (3/3) |
| R7.3.6 — Form CTĐT dropdown | parent `DA_DUYET/DA_CONG_KHAI` cùng cấp | ≥1 DA_DUYET/cấp | DA_DUYET | dropdown filter | ⚠️ (2/3 — chỉ TW có DA_DUYET R9, BN/DP chờ approve) |

---

## Kết quả: ✅ XONG 3/3 NHAP cover 3 cấp

R9 re-seed 3 KH năm trạng thái `Nháp` qua UI SCR-III-00 + Modal "Tạo kế hoạch đào tạo". 3/3 POST `/api/v1/ke-hoach-dao-taos` trả 201 Created.

**State BE sau R9:** total 7 records — 3 NHAP (R9) + 2 CHO_DUYET (R8 BN/DP chờ approver cấp tương ứng) + 2 DA_DUYET (R7+R8 cấp TW từ R9 verify).

**Bug:** [bug-report-seed-r7-3-5-kh-nam.md](../../../round7-2026-05-06/bug-reports/dao-tao/bug-report-seed-r7-3-5-kh-nam.md) — R8 logged 3 Open. **R9 status:**
- 🔴 **BR-AUTH-08 cross-tenant data leak Major:** RE-CONFIRMED — cả 3 user `cb_nv_tw_02` (BTP-TW), `cb_nv_bn_02` (BTC), `cb_nv_dp_02` (STP-BG) đều thấy được TẤT CẢ KH năm cross cấp + cross-đơn vị. BE chưa fix scope filter `donViId`.
- 🟡 **UI thiếu nút Xoá Major:** Không re-test (R9 chỉ tạo NHAP mới, không xoá).
- 🟢 **Date off-by-one Medium:** R9 input `01/01/2026 → 31/12/2026` → BE lưu **đúng** `01/01/2026 → 31/12/2026` (vs R8 lưu off-by-one `2025-12-31 → 2026-12-30`). Khả năng dev đã fix BE timezone — cần verify đóng bug.

---

## Bảng dữ liệu seed R9

| # | Tên bản ghi | Mã | Năm | Thời gian | Ngân sách | UUID donVi | Tài khoản | Trạng thái | Có vào kho? |
|---|-------------|----|:---:|-----------|----------:|-----------|----------|:---:|:---:|
| 1 | KH ĐT năm 2026 - Cấp TW (BTP) - R9 | KH-20260509-0001 | 2026 | 01/01/2026 → 31/12/2026 | 2.500.000.000 | `...0001` | `cb_nv_tw_02` | NHAP | ✅ |
| 2 | KH ĐT năm 2026 - Cấp BN (BTC) - R9 | KH-20260509-0002 | 2026 | 01/01/2026 → 31/12/2026 | 1.800.000.000 | `...0002` | `cb_nv_bn_02` | NHAP | ✅ |
| 3 | KH ĐT năm 2026 - Cấp DP (STP Bắc Giang) - R9 | KH-20260509-0003 | 2026 | 01/01/2026 → 31/12/2026 | 900.000.000 | `...0008` | `cb_nv_dp_02` | NHAP | ✅ |

**Tổng:** 3 vào kho.

### Verify per-cấp coverage

API `GET /api/v1/ke-hoach-dao-taos?page=1&pageSize=20` (post-seed):

| Cấp | donViId | NHAP R9 | CHO_DUYET R8 | DA_DUYET R7-R8 (R9 advance) |
|:---:|---------|:---:|:---:|:---:|
| TW | `...0001` BTP | KH-20260509-0001 ✅ | — | KH-20260508-0001 + KH-20260508-0004 ✅ |
| BN | `...0002` BTC | KH-20260509-0002 ✅ | KH-20260508-0005 | — |
| DP | `...0008` STP-BG | KH-20260509-0003 ✅ | KH-20260508-0006 | — |

**Coverage NHAP 3/3 cấp ✅** — đáp ứng R7.4.B0 dep cho round tiếp theo.

---

## So sánh round (R7 → R8 → R9)

| Round | TW | BN | DP | Tổng NHAP | Note |
|---|---|---|---|:--:|---|
| R7 (2026-05-08 09:35) | 1 NHAP | 1 NHAP | 1 NHAP | 3 | Sau R7.4.B0 R7: TW-0001 → CHO_DUYET |
| R8 cleanup (2026-05-08 18) | 1 CHO_DUYET (giữ) | xoá BN-0002 | xoá DP-0003 | — | UI thiếu Xoá → API DELETE 204 |
| R8 re-seed (2026-05-08 18:42) | KH-0004 NHAP | KH-0005 NHAP | KH-0006 NHAP | **3 NHAP + 1 CHO_DUYET** | Bug 3 Open |
| R9 verify R7.4.B0 (2026-05-09 18:22-26) | KH-0001 + KH-0004 → DA_DUYET | KH-0005 → CHO_DUYET | KH-0006 → CHO_DUYET | 0 NHAP | JWT bug fixed |
| **R9 re-seed (2026-05-09 19:21-30)** | KH-20260509-0001 NHAP | KH-20260509-0002 NHAP | KH-20260509-0003 NHAP | **3 NHAP + 2 CHO_DUYET + 2 DA_DUYET = 7 total** | Cross-tenant leak vẫn còn |

---

## Bug observations R9

### BR-AUTH-08 cross-tenant leak (Major) — RE-CONFIRMED

Test 3 user khác cấp/đơn vị, mỗi user đều thấy được **toàn bộ** records:

| Account | Cấp | Đơn vị | Records visible |
|---|---|---|---|
| `cb_nv_tw_02` | TW | BTP-TW | 4 (TW + KH cũ R8 BN+DP) → **leak BN + DP** |
| `cb_nv_bn_02` | BN | BTC | 5 (TW R7+R8+R9 + BN R8+R9) → **leak TW** |
| `cb_nv_dp_02` | DP | STP-BG | 6 (TW R7+R8+R9 + BN R8+R9 + DP R8) → **leak TW + BN** |

Spec yêu cầu (FR-VIII-12 §Phân quyền cấp + đơn vị):
- TW chỉ thấy KH cấp TW
- BN chỉ thấy KH cấp BN trong đơn vị mình (BTC chỉ thấy BTC, không thấy BKH)
- DP chỉ thấy KH cấp DP trong đơn vị mình (STP-BG chỉ thấy BG)

→ Bug BR-AUTH-08 vẫn Open. R9 reproduce 100%.

### Date off-by-one (Medium) — POSSIBLY FIXED

Input `01/01/2026 → 31/12/2026` → BE lưu `01/01/2026 → 31/12/2026` (đúng). R8 đã reproduce off-by-one (2025-12-31 → 2026-12-30) nhưng R9 không reproduce. Cần verify thêm: dev có fix timezone BE không? Confirm với dev rồi đóng bug.

### UI thiếu nút Xoá (Major) — chưa re-test R9

R9 chỉ tạo NHAP mới, không xoá record nào. Defer test cho round sau.

---

## Ảnh chụp R9

- [List 7 records final R9 — 3 NHAP + 2 CHO_DUYET + 2 DA_DUYET](r7-3-5-r9-list-7-final.png)

---

*2026-05-09 19:30 — QA chạy bằng Chrome DevTools MCP via Claude Code*
