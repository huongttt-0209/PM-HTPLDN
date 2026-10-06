# Test Cases — DM Tình trạng vụ việc (FR-VIII-04, UC102) — Thứ tự + Màu HEX

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-04 · **UC:** UC102
> **Màn hình:** SCR-VIII-01 — Sub-tab "Tình trạng VV"
> **Template:** TPL-DM-CRUD + 2 fields đặc thù: thu_tu **Y bắt buộc** (vs N TPL chuẩn) + mau_hien_thi (HEX)
> **Tham chiếu downstream:** VU_VIEC.tinh_trang_id
> **Tổng số TC:** 11 (10 base + 1 edge A4)

---

## A. Render + Tạo mới fields đặc thù

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TT-001 | qtht_01, env có 7 seed (Mới tiếp nhận, Đang kiểm tra, Đã phân công, Đang xử lý, Chờ bổ sung, Hoàn thành, Từ chối) | Mở tab | List render 7 record sort theo thu_tu ASC; cột Mã/Tên/Thứ tự/Trạng thái + (có thể) badge màu hiển thị | line 260-282 |
| TC-TT-002 | list mở | Verify cột "Mã màu" hoặc preview màu theo mau_hien_thi | Mỗi record có badge/dot màu đúng HEX (vd "Hoàn thành" = #00FF00 xanh) | line 278 |
| TC-TT-003 | [+ Thêm] | ma="TT_TEST", ten="Test TT", thu_tu=99, mau_hien_thi="#FF0000" → Lưu | Tạo OK; list refresh; record xuất hiện cuối list (thu_tu=99) | line 277-278 |
| TC-TT-004 | [+ Thêm], thu_tu= rỗng/null | Lưu | **Validation reject "Thứ tự là bắt buộc"** — SRS line 277 nguyên văn `thu_tu | number | Y | Thứ tự hiển thị trong workflow` (UC102 override TPL N → Y bắt buộc) | line 277 (Y bắt buộc) |
| TC-TT-005 | [+ Thêm], mau_hien_thi="invalid-color" (không phải HEX) | Lưu | Validation reject; hoặc reset về default; verify hành vi | line 278 |
| TC-TT-006 | [+ Thêm], mau_hien_thi="#GGGGGG" (HEX không hợp lệ) | Lưu | Validation reject "Mã màu phải là HEX hợp lệ" | line 278 |
| TC-TT-007 | [+ Thêm], mau_hien_thi=null/empty | Lưu | Cho phép (N — line 278); record không có badge màu | line 278 (N) |
| TC-TT-008 | [+ Thêm], thu_tu=99 (đã có TT khác cùng thu_tu=99) | Lưu | Cho phép trùng thu_tu (sort secondary theo ten); KHÔNG có ràng buộc unique thu_tu | line 86 |

---

## B. Cập nhật / Xóa

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TT-009 | "TT_TEST" tồn tại | Sửa thu_tu 99→1 | Lưu OK; record nhảy lên đầu list (sort thu_tu ASC); audit | line 86 |
| TC-TT-010 | "MOI" (đang dùng cho 50 VU_VIEC) | Xóa | Reject ERR-DM-03 "Đang được sử dụng bởi 50 bản ghi VU_VIEC" | E5 |

---

## C. Edge case bổ sung (A4 inline merge)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-TT-EDGE-001 | "MOI" là current state của 50 VU_VIEC | Click Xóa "MOI" → confirm | ERR-DM-03 message exact "Không thể xóa. Danh mục đang được sử dụng bởi 50 bản ghi VU_VIEC"; record vẫn tồn tại | E5 line 153 |

---

**Tổng số TC:** 11 (10 base + 1 edge)

**Đặc thù vs TPL:**
1. thu_tu BẮT BUỘC (Y) thay vì N default 0
2. mau_hien_thi HEX format
3. Render badge màu trong list
4. ~~DM-03~~ resolved R4: SRS line 277 nguyên văn `thu_tu Y` — UC102 override TPL chung; expected explicit, không cần BA
