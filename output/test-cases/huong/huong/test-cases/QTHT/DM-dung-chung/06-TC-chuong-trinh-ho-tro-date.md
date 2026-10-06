# Test Cases — DM Chương trình hỗ trợ (FR-VIII-03, UC101) — Date range + Đơn vị chủ trì

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-03 · **UC:** UC101
> **Màn hình:** SCR-VIII-01 — Sub-tab "Chương trình HT"
> **Template:** TPL-DM-CRUD + 3 fields đặc thù (thoi_gian_bat_dau Y, thoi_gian_ket_thuc N, don_vi_chu_tri Y)
> **Tham chiếu downstream:** CHUONG_TRINH_HTPL (nhóm XI)
> **Tổng số TC:** 11 (10 base + 1 edge A4)

---

## A. Render + Tạo mới với fields đặc thù

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CT-001 | qtht_01, mở tab Chương trình HT | List render kèm cột thoi_gian_bat_dau, thoi_gian_ket_thuc, don_vi_chu_tri (hoặc trong form chi tiết) | line 234-256, 247-254 |
| TC-CT-002 | [+ Thêm] | ma="CT_2026", ten="Chương trình 2026", thoi_gian_bat_dau=01/01/2026, thoi_gian_ket_thuc=31/12/2026, don_vi_chu_tri="Cục BLDS&KT" → Lưu | Tạo OK; list refresh; audit INSERT | line 247-253 |
| TC-CT-003 | [+ Thêm], thoi_gian_bat_dau= rỗng | Lưu | Validation "Thời gian bắt đầu là bắt buộc" | line 251 (Y) |
| TC-CT-004 | [+ Thêm], thoi_gian_ket_thuc= rỗng (chỉ tg_bat_dau) | Lưu | Cho phép (CT mở vô thời hạn — N tùy chọn) | line 252 (N) |
| TC-CT-005 | [+ Thêm], thoi_gian_bat_dau=01/06/2026, thoi_gian_ket_thuc=01/01/2026 (kết thúc < bắt đầu) | Lưu | Verify: reject hay cho phép? Spec im lặng `[SPEC-CLARIFY-DM-04]` | `[SPEC-CLARIFY-DM-04]` |
| TC-CT-006 | [+ Thêm], don_vi_chu_tri= rỗng | Lưu | Validation "Đơn vị chủ trì là bắt buộc" | line 253 (Y) |

---

## B. Cập nhật / Xóa

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CT-007 | "CT_2026" tồn tại | Sửa thoi_gian_ket_thuc 31/12/2026 → 30/06/2027 | Lưu OK; audit UPDATE old/new dates | BR-DATA-05 |
| TC-CT-008 | "CT_2026" mở | Sửa don_vi_chu_tri | Lưu OK | — |
| TC-CT-009 | "CT_2026" mới tạo, không có CHUONG_TRINH_HTPL.chuong_trinh_id tham chiếu | Xóa | Soft delete OK | BR-DATA-01 |
| TC-CT-010 | "CT_NĐ18_2026" có 5 CHUONG_TRINH_HTPL tham chiếu | Xóa | Reject ERR-DM-03 "Đang được sử dụng bởi 5 bản ghi CHUONG_TRINH_HTPL" | E5 line 256 |

---

## C. Edge case bổ sung (A4 inline merge)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CT-EDGE-001 | "CT_NĐ18_2026" có 5 CHUONG_TRINH_HTPL đang ACTIVE tham chiếu | Mở Sửa CT_NĐ18_2026 đổi thoi_gian_ket_thuc 31/12/2026 → 30/06/2026 | Verify snapshot pattern: HTPL hiện tại giữ thoi_gian cũ HAY auto-update theo CT mới? Spec im lặng `[SPEC-CLARIFY-DM-25]` | BR-CALC-03 (similar SLA snapshot pattern) |

---

**Tổng số TC:** 11 (10 base + 1 edge)

**Đặc thù vs TPL chung:**
1. 3 fields date/text bổ sung
2. Tham chiếu downstream nhóm XI (CT HTPLDN)
3. SPEC-CLARIFY-DM-04: validate thoi_gian_ket_thuc >= thoi_gian_bat_dau?
