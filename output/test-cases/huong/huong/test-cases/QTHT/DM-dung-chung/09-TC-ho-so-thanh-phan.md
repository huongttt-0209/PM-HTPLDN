# Test Cases — DM Hồ sơ đề nghị HT + TT (FR-VIII-08+09, UC106+UC107) — Cấu trúc thành phần

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-08 (HSDN HT), FR-VIII-09 (HSDN TT) · **UC:** UC106 + UC107
> **Màn hình:** SCR-VIII-01 — Sub-tab "Hồ sơ đề nghị HT" + "Hồ sơ đề nghị TT"
> **Template:** TPL-DM-CRUD + structured JSON đặc thù
>   - UC106: thanh_phan_bat_buoc[] + thanh_phan_tuy_chon[] (2 nhóm)
>   - UC107: thanh_phan_ho_so[] (1 nhóm)
> **Tổng số TC:** 16 (15 base + 1 edge A4 — gộp UC106 + UC107 vì pattern tương đương)

---

## A. UC106 — Hồ sơ đề nghị HT (UC106) thanh_phan_bat_buoc + thanh_phan_tuy_chon

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-HS-001 | qtht_01, mở tab "Hồ sơ đề nghị HT" | List render | line 403-419 |
| TC-HS-002 | [+ Thêm] | ma="HS_HT_TEST", ten="Test HSDN HT", thanh_phan_bat_buoc=[{"ten":"Đơn đề nghị","mo_ta":"Mẫu 01"}, {"ten":"Bản sao GDKD"}], thanh_phan_tuy_chon=[{"ten":"Báo cáo tài chính"}] → Lưu | Tạo OK; UI render danh sách thành phần (form repeater hoặc tag-list) | line 416-418 |
| TC-HS-003 | [+ Thêm], thanh_phan_bat_buoc = empty/null | Lưu | Cho phép (N tùy chọn) | line 416 (N) |
| TC-HS-004 | [+ Thêm], thanh_phan_bat_buoc invalid format (string không phải JSON list) | Lưu | Verify hành vi: reject hay parse error? `[SPEC-CLARIFY-DM-12]` | `[SPEC-CLARIFY-DM-12]` |
| TC-HS-005 | [+ Thêm], thanh_phan_bat_buoc[]=20 items | Lưu | Verify cap số items (spec im lặng) | `[SPEC-CLARIFY-DM-12]` |
| TC-HS-006 | "HS_HT_TEST" mở Sửa | Thêm 1 item vào thanh_phan_bat_buoc | Lưu OK; UI list refresh | — |
| TC-HS-007 | "HS_HT_TEST" mở Sửa | Xóa 1 item khỏi thanh_phan_tuy_chon | Lưu OK | — |
| TC-HS-008 | "HS_HT_TEST" mới tạo | Xóa | Soft delete OK | BR-DATA-01 |

---

## B. UC107 — Hồ sơ đề nghị TT (UC107) thanh_phan_ho_so

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-HS-009 | qtht_01, mở tab "Hồ sơ đề nghị TT" | List render | line 422-436 |
| TC-HS-010 | [+ Thêm] | ma="HS_TT_TEST", ten="Test HSDN TT", thanh_phan_ho_so=[{"ten":"Đơn đề nghị thanh toán","mo_ta":"Mẫu 02"}, {"ten":"Hóa đơn"}, {"ten":"Bảng kê"}] → Lưu | Tạo OK | line 433-435 |
| TC-HS-011 | [+ Thêm], thanh_phan_ho_so = empty | Lưu | Cho phép (N tùy chọn) | line 435 (N) |
| TC-HS-012 | "HS_TT_TEST" mở Sửa | Đổi thứ tự items qua UI mechanism khả dụng (drag-drop nếu có / move up-down button / edit field thứ tự) — verify mechanism có sẵn trước khi test | Lưu OK với thứ tự mới; refresh form hiển thị thứ tự mới đã apply. Spec line 435 type "structured" KHÔNG nói rõ UI affordance — log mechanism observed | line 435, `[SPEC-CLARIFY-DM-12]` |
| TC-HS-013 | "HS_TT_TEST" mở Sửa | Item rỗng (ten=null) | Reject hoặc skip; verify | `[SPEC-CLARIFY-DM-12]` |
| TC-HS-014 | "HS_TT_TEST" có HO_SO_CHI_TRA tham chiếu | Xóa | Reject ERR-DM-03 với entity HO_SO_CHI_TRA | E5 |
| TC-HS-015 | "HS_TT_TEST" mới tạo, không tham chiếu | Xóa | Soft delete OK | BR-DATA-01 |

---

## C. Edge case bổ sung (A4 inline merge)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-HS-EDGE-001 | [+ Thêm], thanh_phan_bat_buoc=[{"ten":"Đơn đề nghị"}, {"ten":"Đơn đề nghị"}] (2 items cùng ten) | Lưu | Verify: reject "Tên thành phần không được trùng trong cùng nhóm" hay cho phép duplicate? `[SPEC-CLARIFY-DM-26]` | `[SPEC-CLARIFY-DM-26]` |

---

**Tổng số TC:** 16 (15 base + 1 edge)

**Đặc thù vs TPL:**
1. UC106 có 2 nhóm structured (bắt buộc + tùy chọn)
2. UC107 có 1 nhóm structured
3. UI form yêu cầu repeater/tag-list để nhập danh sách
4. SPEC-CLARIFY-DM-12: JSON shape exact, validate, max items
