# Test Cases — DM Tiêu chí ĐG chi phí (FR-VIII-12, UC110)

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-12 · **UC:** UC110
> **Màn hình:** SCR-VIII-01 — Sub-tab "Tiêu chí ĐG chi phí"
> **Template:** TPL-DM-CRUD (mở rộng) — bổ sung 3 cột (quy_mo_dn / muc_ho_tro_phan_tram / tran_ho_tro_nam) — căn cứ NĐ18/2026
> **Tổng số TC:** 19 (15 base + 2 edge A4 + 2 fill R2)

---

## A. Render danh sách

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCCP-001 | qtht_01, env có 3 tiêu chí seed (Siêu nhỏ 100%/3M, Nhỏ ≤30%/5M, Vừa ≤10%/10M theo NĐ18/2026) | Mở tab | List render với 3 cột bổ sung (Quy mô DN, Mức hỗ trợ %, Trần hỗ trợ/năm); cột Trần format số tiền VNĐ | line 553-571, 1488-1491 |
| TC-TCCP-002 | list mở | Verify cột Trần | Format thousand-separator (vd "3,000,000 VNĐ") | line 568, 1491 |

---

## B. Tạo mới

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCCP-003 | [+ Thêm mới] | ma="TEST_TCCP", ten="Test CP", quy_mo_dn="SIEU_NHO", muc_ho_tro_phan_tram=100, tran_ho_tro_nam=3000000 → Lưu | Tạo OK; list refresh | line 562-569 |
| TC-TCCP-004 | [+ Thêm], quy_mo_dn=null/empty | Lưu | Validation "Quy mô DN là bắt buộc" | line 566 (Y) |
| TC-TCCP-005 | [+ Thêm], quy_mo_dn="DN_LON" (không thuộc enum SIEU_NHO/NHO/VUA) | Lưu | Reject; dropdown chỉ cho 3 enum | line 566 |
| TC-TCCP-006 | [+ Thêm], muc_ho_tro_phan_tram=0 | Lưu | Cho phép (range 0-100, hoặc 0 hợp lệ); verify `[SPEC-CLARIFY-DM-08]` | `[SPEC-CLARIFY-DM-08]` |
| TC-TCCP-007 | [+ Thêm], muc_ho_tro_phan_tram=100 | Lưu | OK | — |
| TC-TCCP-008 | [+ Thêm], muc_ho_tro_phan_tram=150 (>100) | Lưu | Verify `[SPEC-CLARIFY-DM-08]` cap | `[SPEC-CLARIFY-DM-08]` |
| TC-TCCP-009 | [+ Thêm], tran_ho_tro_nam=-1000 (negative) | Lưu | Validation reject `[SPEC-CLARIFY-DM-09]` | `[SPEC-CLARIFY-DM-09]` |
| TC-TCCP-010 | [+ Thêm], tran_ho_tro_nam=0 | Lưu | Cho phép (vd hỗ trợ 0 đồng nghĩa không hỗ trợ chi phí); verify | line 568 |
| TC-TCCP-011 | [+ Thêm], tran_ho_tro_nam=999999999999 (boundary lớn) | Lưu | Verify cap upper (max int hay max money?) | line 568 |

---

## C. Cập nhật / Xóa

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCCP-012 | "TEST_TCCP" tồn tại | Sửa muc_ho_tro_phan_tram 100→80 | Lưu OK; audit UPDATE | BR-DATA-05 |
| TC-TCCP-013 | "TEST_TCCP" mở | Đổi quy_mo_dn từ SIEU_NHO → VUA | Lưu OK | line 566 |
| TC-TCCP-014 | "TEST_TCCP" mới tạo | Xóa | Soft delete OK | BR-DATA-01 |
| TC-TCCP-015 | tiêu chí seed "Nhỏ" (đang dùng cho HSCT chi trả) | Xóa | Reject ERR-DM-03 với entity HO_SO_CHI_TRA hoặc DANH_GIA chi phí | E5 |

---

## D. Edge case bổ sung (A4 inline merge)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCCP-EDGE-001 | [+ Thêm], tran_ho_tro_nam=999999999999 (12 digits ~ 999 tỷ) | Lưu | Verify hành vi: chấp nhận (long money), hiển thị format "999,999,999,999 VNĐ" với separator; hoặc cap upper | line 568 |
| TC-TCCP-EDGE-002 | [+ Thêm], muc_ho_tro_phan_tram=99.5 (decimal) | Lưu | Verify: chấp nhận decimal (number type) hay reject vì spec ngụ ý int? `[SPEC-CLARIFY-DM-24]` | line 567 |

---

## E. Fill gap (R2 Codex review — required negative)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCCP-FILL-001 | qtht_01 mở [+ Thêm], ma/ten/quy_mo_dn/tran_ho_tro_nam OK, **để trống muc_ho_tro_phan_tram** | Submit | Reject với validation "Mức hỗ trợ là bắt buộc" — SRS line 567 đánh Y | line 567 (Y muc_ho_tro_phan_tram) |
| TC-TCCP-FILL-002 | [+ Thêm], ma/ten/quy_mo_dn/muc_ho_tro_phan_tram OK, **để trống tran_ho_tro_nam** | Submit | Reject với validation "Trần hỗ trợ/năm là bắt buộc" — SRS line 568 đánh Y | line 568 (Y tran_ho_tro_nam) |

---

**Tổng số TC:** 19 (15 base + 2 edge A4 + 2 fill R2)

**Đặc thù vs TPL chung:**
1. 3 cột bổ sung Quy mô / Mức / Trần
2. Field quy_mo_dn enum constrained (3 values theo NĐ39/2018: SIEU_NHO/NHO/VUA)
3. Field tran_ho_tro_nam type money (format VNĐ)
4. Tham chiếu downstream: HO_SO_CHI_TRA hoặc DANH_GIA chi phí

**SPEC-CLARIFY:**
- DM-08: muc_ho_tro_phan_tram range cap upper?
- DM-09: tran_ho_tro_nam validate >= 0?
