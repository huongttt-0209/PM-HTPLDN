# Bảng đối chiếu điều kiện — QLBMHD_14 (upload ảnh đại diện hợp lệ bị báo lỗi ".doc/.docx/.xls/.xlsx")

Loại bug: **Validation sai của field "Ảnh đại diện" khi upload ảnh hợp lệ.** Đối tác kỳ vọng field Ảnh đại diện nhận ảnh (.jpg/.png/.gif); thực tế (theo đối tác) khi upload ảnh hợp lệ lại báo lỗi "Chỉ chấp nhận .doc/.docx/.xls/.xlsx" (thông báo vốn thuộc field "File biểu mẫu"). Verdict phụ thuộc: đúng vai trò + đúng field Ảnh đại diện + ảnh upload hợp lệ (định dạng ảnh, ≤5MB).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLBMHD_14.webm + Excel row 107) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Field upload | **Ảnh đại diện** (helper: ".jpg, .png, .gif", tối đa 1 tệp ≤5MB) | Đúng field "Ảnh đại diện" trên form Sửa (helper y hệt ".jpg, .png, .gif ≤5MB/tệp") | Không |
| Loại file upload | **Ảnh hợp lệ** (ảnh đại diện) | `test-avatar.png` — PNG hợp lệ 236 B (đúng định dạng ảnh field cho phép) | Không |
| Màn kiểm | Form Chỉnh sửa/Thêm biểu mẫu (`/bieu-mau/<id>/sua`) | Form Chỉnh sửa `/bieu-mau/28104008.../sua` (BM-20260715-001) | Không |

**Kết luận: 0 GAP. Tái hiện: KHÔNG.**

Trên build hiện tại (`18.143.165.120.nip.io`, ngày 2026-07-20), upload ảnh PNG hợp lệ vào field "Ảnh đại diện" được **CHẤP NHẬN đầy đủ**, KHÔNG hề xuất hiện lỗi ".doc/.docx/.xls/.xlsx" ở bất kỳ bước nào:

- **Client accept:** file vào danh sách "test-avatar.png (236 B) · Xem · Xóa", item không có class `error` (`errorState=false`); toast observer (không dedupe) chỉ bắt được list-item thành công, không bắt được thông báo lỗi định dạng; `.ant-message-notice / .ant-form-item-explain-error` rỗng.
- **BE nhận file:** `POST /api/v1/bieu-maus/upload?loai=anh-dai-dien` → **201 Created**.
- **Lưu form:** `PATCH /api/v1/bieu-maus/28104008-7b0d-4783-9825-a188ad11a289` → **200 OK**, redirect về `/bieu-mau/danh-sach` (lưu thành công).
- Evidence: `reverify-audit/QLBMHD_14/QLBMHD_14-avatar-accepted.png` (screenshot field Ảnh đại diện đã nhận test-avatar.png) + network trace 201/200.

Đối chiếu SRS / helper:
- Field "Ảnh đại diện" trên form (SCR-VII-02) tự khai định dạng cho phép ".jpg, .png, .gif" — hành vi build hiện tại (nhận PNG) **khớp** khai báo field, KHÔNG áp nhầm validator ".doc/.docx/.xls/.xlsx" của field "File biểu mẫu".

→ **`Reject`** (không tái hiện): lỗi đối tác phản ánh (upload ảnh đại diện bị chặn bằng thông báo định dạng .doc/.xls) KHÔNG còn xảy ra trên build hiện tại; field Ảnh đại diện xử lý ảnh đúng. Nhiều khả năng bản đối tác test (env `htpldn-uat.ospgroup.vn`, 2026-07-13) là build cũ đã bị wire nhầm validator, nay đã sửa. Nếu đối tác vẫn gặp trên bản mới nhất → gửi lại video + tên/định dạng/kích thước file cụ thể để re-verify.

Chi tiết: bug KHÔNG log (Reject); không tạo bug-report entry.
