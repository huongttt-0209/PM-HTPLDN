# A4 — Edge Case Hunter Audit Log (DM Dùng Chung)

> **Date:** 2026-05-08
> **Mode:** Proposal + Inline merge mapping (audit only — TC mới đã được Edit trực tiếp vào file UC tương ứng)
> **Reference:** [`plan.md` §3.1 A4 inline merge rule](../../../tasks/detailed-tc/plan.md), CLAUDE.md Iron Rule.

## Tổng quan

A4 phát hiện **18 edge case** beyond A3 base coverage. Tất cả đã merge inline vào file UC tương ứng (xem cột "Merged To"). File 08 này CHỈ là audit log — KHÔNG phải TC source.

---

## Edge case proposal + merge mapping

### Group 1 — TPL-DM-CRUD chung (merge vào file 01)

| # | Edge case | Lý do quan trọng | TC mới | Merged To | Status |
|---|---|---|---|---|---|
| E1 | Concurrency: 2 QTHT cùng tạo ma trùng (race condition) | Production risk — DB unique constraint phải bắt được; UX cần thông báo rõ | TC-LV-EDGE-001 | `01-TC-tpl-dm-CRUD-representative-LV-PL.md` Section H | ✅ merged |
| E2 | Unicode/diacritic Vietnamese trong ten (vd "Đào tạo / Bồi dưỡng") | Spec dùng tiếng Việt, charset UTF-8; verify input + output preserve | TC-LV-EDGE-002 | File 01 Section H | ✅ merged |
| E3 | Whitespace leading/trailing trong ma + ten (vd " THUE ") | Common UX bug — backend trim, FE không trim → false unique conflict | TC-LV-EDGE-003 | File 01 Section H | ✅ merged |
| E4 | Soft-deleted record + re-create cùng ma | BR-DATA-01 soft delete; ma vẫn unique trong DB → re-create phải reject hoặc reuse soft-deleted? | TC-LV-EDGE-004 | File 01 Section H | ✅ merged |
| E5 | Rich text/HTML/script trong mo_ta | XSS risk — mo_ta hiển thị truncate, có sanitize không? | TC-LV-EDGE-005 | File 01 Section H | ✅ merged |
| E6 | Search keyword với regex special chars (`.\^$()[]{}*+?|`) | BR-EC-13 sanitize — verify escape regex | TC-LV-EDGE-006 | File 01 Section H | ✅ merged |
| E7 | Pagination boundary: record thứ 21 (boundary on-bound 20/page) | BR-DATA-07 — verify trang 1 chỉ 20, trang 2 record 21+ | TC-LV-EDGE-007 | File 01 Section H | ✅ merged |
| E8 | Sort secondary với cùng thu_tu (line 86 secondary ten ASC) | Verify deterministic ordering | TC-LV-EDGE-008 | File 01 Section H | ✅ merged |

### Group 2 — Cơ quan ĐV (merge vào file 03)

| # | Edge case | Lý do | TC mới | Merged To | Status |
|---|---|---|---|---|---|
| E9 | UC103 đổi cap TW root → BN/DP khi có children | BR-AUTH-02 vi phạm — children sẽ mất cha hợp lệ; phải reject hoặc cascade | TC-CQDV-EDGE-001 | `03-TC-co-quan-don-vi-tree-2tier.md` Section G | ✅ merged |
| E10 | UC103 performance — TW có 50+ BN/DP children, expand toàn bộ | NFR performance check; verify lazy load hoặc virtualize tree | TC-CQDV-EDGE-002 | File 03 Section G | ✅ merged |
| E11 | UC103 don_vi với TAI_KHOAN đang đăng nhập + đổi trang_thai TAM_DUNG | Race — TK đang session active có bị đá không? | TC-CQDV-EDGE-003 | File 03 Section G | ✅ merged |

### Group 3 — Tiêu chí ĐG hiệu quả (merge vào file 04)

| # | Edge case | Lý do | TC mới | Merged To | Status |
|---|---|---|---|---|---|
| E12 | UC109 toggle trang_thai — label tổng auto-update? | Spec line 542 nói "tổng tiêu chí HOẠT ĐỘNG" — verify reactive | TC-TCHQ-EDGE-001 | `04-TC-tieu-chi-dg-hieu-qua.md` Section E | ✅ merged |
| E13 | UC109 thang_diem_min và max bằng nhau ở UPDATE (đổi từ 1/10 → 5/5) | ERR-TC-01 phải bắt cả lúc UPDATE, không chỉ CREATE | TC-TCHQ-EDGE-002 | File 04 Section E | ✅ merged |

### Group 4 — Tiêu chí ĐG chi phí (merge vào file 05)

| # | Edge case | Lý do | TC mới | Merged To | Status |
|---|---|---|---|---|---|
| E14 | UC110 tran_ho_tro_nam = 999,999,999,999 (12 digits) | Format VNĐ overflow — verify hiển thị thousand separator | TC-TCCP-EDGE-001 | `05-TC-tieu-chi-dg-chi-phi.md` Section D | ✅ merged |
| E15 | UC110 muc_ho_tro_phan_tram = 99.5 (decimal) | Spec không nói int/float — verify hành vi | TC-TCCP-EDGE-002 | File 05 Section D | ✅ merged |

### Group 5 — Chương trình HT (merge vào file 06)

| # | Edge case | Lý do | TC mới | Merged To | Status |
|---|---|---|---|---|---|
| E16 | UC101 sửa thoi_gian_bat_dau khi CHUONG_TRINH_HTPL đang dùng (snapshot?) | Cascade snapshot pattern (như BR-CALC-03 SLA); verify HTPL hiện tại có giữ nguyên thoi_gian cũ không | TC-CT-EDGE-001 | `06-TC-chuong-trinh-ho-tro-date.md` Section C | ✅ merged |

### Group 6 — Tình trạng VV (merge vào file 07)

| # | Edge case | Lý do | TC mới | Merged To | Status |
|---|---|---|---|---|---|
| E17 | UC102 xóa TT đang là current state của 50 VU_VIEC | ERR-DM-03 — verify cascade message exact | TC-TT-EDGE-001 | `07-TC-tinh-trang-vv-mau.md` Section C | ✅ merged |

### Group 7 — Hồ sơ thành phần (merge vào file 09)

| # | Edge case | Lý do | TC mới | Merged To | Status |
|---|---|---|---|---|---|
| E18 | UC106/107 thanh_phan items có ten duplicate | Spec không nói unique trong array — verify reject hoặc cho phép | TC-HS-EDGE-001 | `09-TC-ho-so-thanh-phan.md` Section C | ✅ merged |

---

## Tổng kết A4

- **Proposed:** 18 edge cases
- **Merged inline:** 18/18 ✅ (100%)
- **Reject:** 0
- **TC count delta:** +18 (228 → 246 sau A4)

**Ghi chú:** TC mới đặt prefix `EDGE-` để dễ trace. ID khôi phục theo prefix file (vd TC-LV-EDGE-001..008 cho file 01, TC-CQDV-EDGE-001..003 cho file 03).
