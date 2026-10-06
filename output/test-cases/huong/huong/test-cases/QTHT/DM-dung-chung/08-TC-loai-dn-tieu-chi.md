# Test Cases — DM Loại doanh nghiệp (FR-VIII-07, UC105) — Tiêu chí doanh thu/lao động

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-07 · **UC:** UC105
> **Màn hình:** SCR-VIII-01 — Sub-tab "Loại doanh nghiệp"
> **Template:** TPL-DM-CRUD + 2 fields tiêu chí (tieu_chi_doanh_thu N, tieu_chi_lao_dong N) — căn cứ NĐ39/2018
> **Tham chiếu downstream:** DOANH_NGHIEP.loai_doanh_nghiep_id
> **Tổng số TC:** 10

---

## A. Render + Tạo mới fields đặc thù

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-LDN-DEEP-001 | qtht_01, env seed 3 record (DN siêu nhỏ/nhỏ/vừa) | Mở tab | List 3 record với cột tieu_chi_doanh_thu, tieu_chi_lao_dong (text long) | line 382-399, line 393-396 |
| TC-LDN-DEEP-002 | [+ Thêm] | ma="LDN_TEST", ten="Test loại DN", tieu_chi_doanh_thu="< 10 tỷ VNĐ", tieu_chi_lao_dong="< 30 người" → Lưu | Tạo OK; audit INSERT | line 393-396 |
| TC-LDN-DEEP-003 | [+ Thêm], tieu_chi_doanh_thu= rỗng | Lưu | Cho phép (N tùy chọn); record vẫn tạo OK | line 395 (N) |
| TC-LDN-DEEP-004 | [+ Thêm], tieu_chi_lao_dong= rỗng | Lưu | Cho phép | line 396 (N) |
| TC-LDN-DEEP-005 | [+ Thêm], tieu_chi_doanh_thu = string 1000 ký tự | Lưu | Verify max length text — spec im lặng — verify hành vi `[SPEC-CLARIFY-DM-19]` | `[SPEC-CLARIFY-DM-19]` |
| TC-LDN-DEEP-006 | [+ Thêm], ma="SIEU_NHO" (trùng seed) | Lưu | ERR-DM-01 trùng | E3 |

---

## B. Cập nhật / Xóa

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-LDN-DEEP-007 | "LDN_TEST" tồn tại | Sửa tieu_chi_doanh_thu | Lưu OK; audit UPDATE | BR-DATA-05 |
| TC-LDN-DEEP-008 | "LDN_TEST" mở | Sửa ten | Lưu OK; tieu_chi giữ nguyên | — |
| TC-LDN-DEEP-009 | "LDN_TEST" mới tạo, không có DOANH_NGHIEP tham chiếu | Xóa | Soft delete OK | BR-DATA-01 |
| TC-LDN-DEEP-010 | "SIEU_NHO" có 100 DOANH_NGHIEP.loai_doanh_nghiep_id tham chiếu | Xóa | Reject ERR-DM-03 "Đang được sử dụng bởi 100 bản ghi DOANH_NGHIEP" | E5 |

---

**Tổng số TC:** 10 (TC-LDN-DEEP-001..010 — prefix `LDN-DEEP-` resolved ID conflict với file 02 smoke `TC-LDN-001..005` ở A7)

**Đặc thù vs TPL:**
1. 2 fields text NĐ39/2018 (tieu_chi_doanh_thu + tieu_chi_lao_dong)
2. Tham chiếu downstream DOANH_NGHIEP

**SPEC-CLARIFY:**
- DM-19: Max length text tieu_chi?
