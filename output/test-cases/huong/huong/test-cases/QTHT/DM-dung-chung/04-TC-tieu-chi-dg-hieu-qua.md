# Test Cases — DM Tiêu chí ĐG hiệu quả (FR-VIII-11, UC109)

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-11 · **UC:** UC109
> **Màn hình:** SCR-VIII-01 — Sub-tab "Tiêu chí ĐG hiệu quả"
> **Template:** TPL-DM-CRUD (mở rộng) — bổ sung 3 cột (trong_so / thang_diem_min / thang_diem_max) + label "Tổng: {X}%"
> **BR critical:** BR-CALC-04 (tổng trọng số = 100%) + WRN-TC-01 (warning, vẫn cho lưu) + ERR-TC-01 (validate min < max)
> **Tổng số TC:** 24 (18 base + 2 edge A4 + 4 fill R2)

---

## A. Render danh sách + label tổng

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCHQ-001 | qtht_01, env có 5 tiêu chí seed (tổng trong_so = 100%) | Mở tab "Tiêu chí ĐG hiệu quả" | List render 8 cột (Mã/Tên/Mô tả/Thứ tự/Trọng số/Min/Max/Trạng thái/Hành động); label dưới list "Tổng: 100%" hiển thị **MÀU XANH** | line 519-549, line 1480-1485 |
| TC-TCHQ-002 | env có 5 tiêu chí, tổng = 80% (chưa đủ 100%) | Mở list | Label "Tổng: 80%" hiển thị **MÀU ĐỎ** | line 1485 |
| TC-TCHQ-003 | env có tiêu chí với trang_thai=Vô hiệu hóa | Mở list | Label tổng tính chỉ trên tiêu chí HOẠT ĐỘNG (theo line 542 "tiêu chí hoạt động") | line 541-543 |

---

## B. Tạo mới tiêu chí

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCHQ-004 | tổng hiện tại 80%, [+ Thêm mới] | ma="TC_06", ten="Tiêu chí 6", trong_so=20, thang_diem_min=1, thang_diem_max=10 → Lưu | Tạo OK; list refresh; label tổng update lên 100% màu xanh | line 532-535 |
| TC-TCHQ-005 | tổng hiện tại 100%, [+ Thêm], trong_so=10 (sẽ vượt thành 110%) | Lưu | Lưu OK kèm WRN-TC-01 "Tổng trọng số hiện tại: 110%. Cần đảm bảo = 100% trước khi sử dụng" — vẫn cho lưu | E1 WRN line 548 |
| TC-TCHQ-006 | [+ Thêm], trong_so=0 | Lưu | Cho phép (range 0-100); audit OK | line 532 |
| TC-TCHQ-007 | [+ Thêm], trong_so=100 | Lưu | Cho phép | line 532 |
| TC-TCHQ-008 | [+ Thêm], trong_so=-5 (negative) | Lưu | **Validation reject "Trọng số phải trong khoảng 0-100"** — SRS line 532 nguyên văn `trong_so | Y | 0-100%, tổng tất cả tiêu chí = 100%` → range [0,100] explicit; negative ngoài range → reject | line 532 (range 0-100%) |
| TC-TCHQ-009 | [+ Thêm], trong_so=150 (>100) | Lưu | **Reject với "Trọng số phải trong khoảng 0-100"** — line 532 cap range explicit. WRN-TC-01 chỉ áp dụng khi tổng != 100% từ các giá trị valid (mỗi giá trị 0-100); KHÔNG áp dụng cap upper cho tổng. | line 532 (range 0-100% — input cap), WRN-TC-01 chỉ cho tổng |

---

## C. Validate thang điểm min/max

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCHQ-010 | [+ Thêm], thang_diem_min=5, thang_diem_max=5 (bằng nhau) | Lưu | ERR-TC-01 "Điểm tối thiểu phải nhỏ hơn điểm tối đa" | E2 line 549 |
| TC-TCHQ-011 | [+ Thêm], thang_diem_min=10, thang_diem_max=5 (đảo ngược) | Lưu | ERR-TC-01 | E2 |
| TC-TCHQ-012 | [+ Thêm], thang_diem_min=1, thang_diem_max=10 | Lưu | OK | line 533-534 |
| TC-TCHQ-013 | [+ Thêm], thang_diem_min=1, thang_diem_max=1000 | Lưu | Verify cap upper bound `[SPEC-CLARIFY-DM-06]` | `[SPEC-CLARIFY-DM-06]` |
| TC-TCHQ-014 | [+ Thêm], thang_diem_min=-5 (negative) | Lưu | Verify: cho phép negative không? Spec im lặng | line 533 |

---

## D. Cập nhật / Xóa

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCHQ-015 | tiêu chí "TC_01" có trong_so=20 | Sửa trong_so=30 → Lưu | Lưu OK; audit UPDATE old=20 → new=30; label tổng cập nhật | BR-DATA-05 |
| TC-TCHQ-016 | "TC_01" mở Sửa, đổi thang_diem_min=5 trong khi max=4 | Lưu | ERR-TC-01 reject | E2 |
| TC-TCHQ-017 | tiêu chí "TC_06" mới tạo, không có DANH_GIA tham chiếu | Xóa | Soft delete OK; label tổng giảm | BR-DATA-01 |
| TC-TCHQ-018 | tiêu chí có DANH_GIA.tieu_chi_id tham chiếu | Xóa | Reject ERR-DM-03 "Đang được sử dụng bởi N bản ghi DANH_GIA" | E5 |

---

## E. Edge case bổ sung (A4 inline merge)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCHQ-EDGE-001 | tổng đang 100% (5 tiêu chí kích hoạt), tiêu chí "TC_03" trong_so=20 | Sửa "TC_03" trang_thai = Vô hiệu hóa | Lưu OK; label tổng auto-update xuống 80% (chỉ tiêu chí HOẠT ĐỘNG được tính); badge đỏ vì != 100% | line 541-542 |
| TC-TCHQ-EDGE-002 | "TC_03" tồn tại với min=1, max=10 | Mở Sửa, đổi min=10, max=5 (đảo ngược) | ERR-TC-01 reject ở UPDATE (không chỉ CREATE); validation consistent | E2 line 549, BR-DATA-03 |

---

## F. Fill gap (R2 Codex review — required negative + WRN sau save)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TCHQ-FILL-001 | qtht_01 mở [+ Thêm], điền ten + ma + min/max OK, **để trống trong_so** | Submit | Reject với validation "Trọng số là bắt buộc" — SRS line 532 đánh Y bắt buộc | line 532 (Y trong_so) |
| TC-TCHQ-FILL-002 | [+ Thêm], điền ten/ma/trong_so/max OK, **để trống thang_diem_min** | Submit | Reject "Thang điểm tối thiểu là bắt buộc" — line 533 Y | line 533 (Y thang_diem_min) |
| TC-TCHQ-FILL-003 | [+ Thêm], điền ten/ma/trong_so/min OK, **để trống thang_diem_max** | Submit | Reject "Thang điểm tối đa là bắt buộc" — line 534 Y | line 534 (Y thang_diem_max) |
| TC-TCHQ-FILL-004 | env có 5 tiêu chí HOẠT ĐỘNG tổng = 100% | Disable 1 tiêu chí (trong_so=20) → trang_thai=Vô hiệu hóa → Lưu | Lưu OK; **trigger WRN-TC-01** "Tổng trọng số hiện tại: 80%. Cần đảm bảo = 100% trước khi sử dụng" — warning kích hoạt **sau save** không chỉ display label, vì spec line 542 yêu cầu kiểm tra mỗi tạo/cập nhật | line 541-543 (kiểm tra sau mỗi tạo/cập nhật), WRN-TC-01 line 548 |

---

**Tổng số TC:** 24 (18 base + 2 edge A4 + 4 fill R2)

**Đặc thù vs TPL chung:**
1. 3 cột bổ sung Trọng số / Min / Max
2. Label "Tổng: {X}%" với màu xanh/đỏ theo BR-CALC-04
3. BR-CALC-04 cảnh báo (vẫn cho lưu) thay vì reject
4. ERR-TC-01 validate min < max
5. WRN-TC-01 warning vs ERR

**SPEC-CLARIFY:**
- DM-05: Range trong_so 0-100 hay không cap?
- DM-06: thang_diem_max upper cap?
- DM-07: BR-CALC-04 có cap upper khi tổng > X%?
