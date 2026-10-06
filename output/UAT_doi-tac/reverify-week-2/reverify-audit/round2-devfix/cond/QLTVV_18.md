# Bảng đối chiếu điều kiện — QLTVV_18 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Màn hình | Form Thêm mới TVV, mục "File đính kèm (Bằng cấp/Chứng chỉ)" (tối đa 10 tệp .pdf) | Đúng uploader File đính kèm, giới hạn 10 tệp | Không |
| Thao tác | Tải lên vượt 10 tệp PDF (thêm tệp thứ 11) | Đã 10 tệp trong danh sách → thêm tệp thứ 11; và thử chọn 11 tệp cùng lúc | Không |
| Kết quả kỳ vọng | Hiển thị thông báo lỗi khi vượt số lượng cho phép | Danh sách giữ 10 tệp (tệp thứ 11 bị chặn) + hiện thông báo "Chỉ được tải tối đa 10 tệp." | Không |
