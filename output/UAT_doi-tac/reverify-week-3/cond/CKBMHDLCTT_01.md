# Bảng đối chiếu điều kiện — CKBMHDLCTT_01

Loại bug: **Trường "Ảnh đại diện" (khi công khai biểu mẫu) từ chối ảnh hợp lệ với lỗi "chỉ chấp nhận .doc/.docx/.xls/.xlsx".** Verdict phụ thuộc: app có nhận ảnh .jpg/.png ở trường Ảnh đại diện không.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (TW/BN/ĐP) | CB Nghiệp vụ (`cbnv_bn`) — nằm trong tập vai trò case chỉ định | Không |
| Màn hình | Sửa biểu mẫu → bật "Công khai trên Cổng PLQG" → trường "Ảnh đại diện" | Cùng màn (`/bieu-mau/{id}/sua`) | Không |
| Nhãn trường | ".jpg, .png, .gif — tối đa 5MB" | Nhãn y hệt | Không |
| Thao tác | Upload ảnh `.jpg` hợp lệ vào Ảnh đại diện | Upload ảnh `.png` (400×300) + `.jpg` (400×300) hợp lệ | Không |

**Kết luận: không tái hiện.** Trên bản kiểm thử hiện tại, trường Ảnh đại diện NHẬN ảnh hợp lệ (.png + .jpg): đính kèm + nút Xem/Xóa, Lưu (sau khi công khai thư mục cha) thành công → chi tiết biểu mẫu hiển thị "Ảnh đại diện: BM-B6-avatar..." (lưu server-side OK). KHÔNG còn thông báo "chỉ chấp nhận .doc/.docx/.xls/.xlsx". Kết quả quan sát khác hẳn claim đối tác (đối tác: bị từ chối; mình: được nhận) → claim không còn đúng trên bản hiện tại. → **Reject**. Bằng chứng: `BUG-CKBMHDLCTT_01-anh-dai-dien-accepts-png.png`, `BUG-CKBMHDLCTT_01-detail-anh-dai-dien-persisted.png`.

> Ghi chú nội bộ (không đưa vào note đối tác): bằng chứng đối tác `CKBMHDLCTT_01.webm` (t021s) cho thấy lỗi CÓ THẬT trên bản đối tác test — upload `.jpg` báo đúng "Biểu mẫu chỉ chấp nhận file .doc, .docx, .xls, .xlsx". Cụm lỗi liên quan QLBMHD_03/11 (b4) + QLBMHD_14 (b5). Nay đã fix trên bản hiện tại. Vai trò: case chỉ định "CB Nghiệp vụ TW/BN/ĐP" — `cbnv_bn` nằm trong tập này nên đúng vai trò; trường Ảnh đại diện là validate client-side, không phụ thuộc đơn vị.
