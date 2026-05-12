# Module classification matrix — 18 module PM HTPLDN

> **Generated:** 2026-05-12 11:45:00 (Phase 0)
> **Nguồn:** [`list-module.md`](../list-module.md) · [`tasks/system-overview.md`](../../../tasks/system-overview.md) §4 · [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)
>
> **Cách dùng:** Plan Drafter (Phase 1) đọc cột "SRS local path" + "Upstream cần seed" để biết phạm vi đọc + dependency. Tester pick up (sau khi plan execute xong) đọc "Nhóm Rule 4" để biết delta intensity.

---

## 18 module × 9 thuộc tính

| # | Slug | FR | Tên module | Tầng | SCR | v3.5? | Nhóm Rule 4 | Complexity | SRS local path (đọc khi draft) | Upstream cần seed |
|:-:|---|:-:|---|:-:|---|:-:|:-:|:-:|---|---|
| 1 | `fr-10-qtht` | FR-10 | Quản trị hệ thống | 1 | SCR-VIII-01..10 | ✅ FULL | A | L | `srs-v3/srs-fr-10-quan-tri.md` + `srs-update-2026-5-5/srs-fr-10-quan-tri.md` + `srs-update-2026-5-5/_DELTA-MAP-FR10.md` | — (nền) |
| 2 | `fr-07-doanh-nghiep` | FR-07 | Doanh nghiệp | 2 | SCR-V.III-01/02/03 | ✅ | B | M | `srs-v3/srs-fr-07-doanh-nghiep.md` + `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md` + `_DELTA-MAP-FR07.md` | fr-10-qtht (DM LOAI_DN, DON_VI, TINH_THANH) |
| 3 | `fr-04-chuyen-gia-tvv` | FR-04 | CG/TVV/NHT/TC-TV | 2 | SCR-IV-01/02/03 + SCR-IV-NEW-01..03 + SCR-IV-NHT-01..03 | ✅ FULL (NHT lifecycle + TCTV approval mới v3.5) | A | L | `srs-v3/srs-fr-04-chuyen-gia-tvv.md` + `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` + `_DELTA-MAP-FR04.md` | fr-10-qtht (DM LINH_VUC_PL, DON_VI; TAI_KHOAN) |
| 4 | `fr-09-bieu-mau` | FR-09 | Biểu mẫu | 2 | SCR-VII-01/02/03 | ✅ | B | M | `srs-v3/srs-fr-09-bieu-mau.md` + `srs-update-2026-5-5/srs-fr-09-bieu-mau.md` + `_DELTA-MAP-FR09.md` | fr-10-qtht (DM LINH_VUC_PL) |
| 5 | `fr-15-ct-htpldn` | FR-15 | CT HTPLDN GĐ1 (KH) + GĐ2 (Đợt BC) | 2+5 | SCR-XI-01 (2 tab) | ❌ (giữ v3) | C | M | `srs-v3/srs-fr-15-ct-htpldn.md` (only) | fr-10-qtht, fr-07-doanh-nghiep |
| 6 | `ho-so-doi-mat-khau` | cross | Hồ sơ + đổi mật khẩu | — | (cross-module) | ✅ (v3.5 spec mới) | A | S | `srs-update-2026-5-5/ho-so-doi-mat-khau.md` + `srs-update-2026-5-5/_DELTA-MAP-PROFILE-PWD.md` | fr-10-qtht (TAI_KHOAN) |
| 7 | `cross-cutting-permission` | cross | Permission matrix + state machine | — | (cross-module) | A | A | M | `srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md` + `output/permission-matrix.md` | fr-10-qtht + ALL |
| 8 | `fr-05-vu-viec` | FR-05 | Vụ việc TGPL | 3 | SCR-V.I-01/02/03 | ✅ FULL (2-tier permission v3.5) | A | XL | `srs-v3/srs-fr-05-vu-viec.md` + `srs-update-2026-5-5/srs-fr-05-vu-viec.md` + `_DELTA-MAP-FR05.md` | fr-10, fr-07, fr-04, fr-09 |
| 9 | `fr-02-hoi-dap` | FR-02 | Hỏi đáp | 3 | SCR-II-01/02/03 | ✅ FULL (BR-FLOW-01 auto + bỏ phân công mặc định Q11) | A | L | `srs-v3/srs-fr-02-hoi-dap.md` + `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` | fr-10, fr-04 |
| 10 | `fr-12-tv-chuyen-sau` | FR-12 | Tư vấn pháp luật chuyên sâu (rename v3.5) | 3 | SCR-X1-01/02 | ✅ | B | L | `srs-v3/srs-fr-12-tv-chuyen-sau.md` + `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md` + `_DELTA-MAP-FR12.md` | fr-10, fr-04, fr-07 |
| 11 | `fr-03-dao-tao` | FR-03 | Đào tạo (4 sub-menu) | 3 | SCR-III-01..05 | ✅ | B | L | `srs-v3/srs-fr-03-dao-tao.md` + `srs-update-2026-5-5/srs-fr-03-dao-tao.md` + `_DELTA-MAP-FR03.md` | fr-10, fr-04, fr-07 |
| 12 | `fr-14-hop-dong-tv` | FR-14 | Hợp đồng tư vấn | 4 | SCR-X3-01 | ❌ (giữ v3) | C | M | `srs-v3/srs-fr-14-hop-dong-tv.md` (only) | fr-04, fr-05 |
| 13 | `fr-06-chi-tra` | FR-06 | Chi trả chi phí | 4 | SCR-V.II-01/02 | ✅ FULL (DN bổ sung HSCT mới v3.5) | A | XL | `srs-v3/srs-fr-06-chi-tra.md` + `srs-update-2026-5-5/srs-fr-06-chi-tra.md` + `_DELTA-MAP-FR06.md` | fr-05, fr-14, fr-07 |
| 14 | `fr-13-tv-nhanh` | FR-13 | TV nhanh — Phiên + Kho QA | 4 | SCR-X2-01/03 | ✅ FULL | A | L | `srs-v3/srs-fr-13-tv-nhanh.md` + `srs-update-2026-5-5/srs-fr-13-tv-nhanh.md` | fr-02, fr-12 |
| 15 | `fr-08-danh-gia-hq` | FR-08 | Theo dõi Đánh giá HQ HTPL (rename v3.5) | 4 | SCR-VI-01 (4 tab) | ✅ FULL (rename + FR-VI-10 read-only mới) | A | L | `srs-v3/srs-fr-08-danh-gia.md` + `srs-update-2026-5-5/srs-fr-08-danh-gia.md` + `_DELTA-MAP-FR08.md` | fr-10, fr-05 |
| 16 | `fr-11-bao-cao` | FR-11 | Báo cáo 23 loại | 5 | SCR-IX-01 | ❌ (giữ v3) | D | M | `srs-v3/srs-fr-11-bao-cao.md` (only) | ALL upstream |
| 17 | `fr-01-dashboard` | FR-01 | Dashboard 9 KPI + 2 chart | 5 | SCR-I-01 | ✅ | C | M | `srs-v3/srs-fr-01-dashboard.md` + `srs-update-2026-5-5/srs-fr-01-dashboard.md` | ALL upstream |
| 18 | `fr-16-api` | FR-16 | API kết nối Cổng PLQG (18 outbound + ~8 inbound) | 5 | (no UI) | ❌ (giữ v3) | D | M | `srs-v3/srs-fr-16-api.md` (only) | ALL upstream |

---

## Phase 1 batch order (theo tầng dependency)

> Batch A → B → C → D chạy tuần tự, mỗi batch spawn 4-5 subagent parallel.

### Batch A — Tầng 1+2 (foundation/master data) — 5 module, ~30-45 phút
1. `fr-10-qtht` (L)
2. `fr-07-doanh-nghiep` (M)
3. `fr-04-chuyen-gia-tvv` (L)
4. `fr-09-bieu-mau` (M)
5. `fr-15-ct-htpldn` (M)

### Batch B — Tầng 3 + Cross-cutting — 5 module, ~30-45 phút
6. `fr-05-vu-viec` (XL)
7. `fr-02-hoi-dap` (L)
8. `fr-12-tv-chuyen-sau` (L)
9. `fr-03-dao-tao` (L)
10. `ho-so-doi-mat-khau` (S)

### Batch C — Tầng 4 + Cross-cutting — 5 module, ~30-45 phút
11. `fr-14-hop-dong-tv` (M)
12. `fr-06-chi-tra` (XL)
13. `fr-13-tv-nhanh` (L)
14. `fr-08-danh-gia-hq` (L)
15. `cross-cutting-permission` (M)

### Batch D — Tầng 5 (output/reporting) — 3 module, ~20-30 phút
16. `fr-11-bao-cao` (M)
17. `fr-01-dashboard` (M)
18. `fr-16-api` (M)

---

## Convention nhóm Rule 4 (informational only)

| Nhóm | Ý nghĩa cho tester pick up sau plan |
|:-:|---|
| **A FULL** | Module có file SRS update v3.5 đụng MỚI (rename, lifecycle mới, feature mới). Tester chạy FULL test khi pick up — workflow + functional + permission. |
| **B DELTA+IMPACT** | Có v3.5 update nhưng impact giới hạn. Test phần delta đầy đủ + sample workflow happy path. |
| **C IMPACT only** | KHÔNG có file v3.5 riêng nhưng chịu impact cross-cutting (UC renumber, hard-delete, 5 trường công khai). Sample 2-3 màn đại diện. |
| **D SKIP / smoke** | Module ổn định, không update v3.5, smoke 5 phút verify còn login + render được. |

Source: CLAUDE.md user-level "Rule 4 — Khi nhận SRS update".

---

## Verification (Phase 0 acceptance)

- [x] 18 dòng module liệt kê
- [x] Mỗi module có SRS local path cite (prefix `srs-v3/` hoặc `srs-update-2026-5-5/`)
- [x] Mỗi module có "Upstream cần seed" để inform Phase 3 cross-link
- [x] 4 batch Phase 1 chia rõ ràng theo tầng dependency
