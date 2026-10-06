# Bảng đối chiếu điều kiện — re-verify QLKTLBG_02 (row 8, mode reverify2, 30/07/2026)

Bug gốc (vòng 2, đối tác): "Hệ thống hiển thị thiếu các trường thông tin: Ảnh xem trước, Lĩnh vực,
Người tạo" — bảng Kho tài liệu / Bài giảng chỉ 6 cột. BA chốt 30/07/2026 là bug thật (Major),
dev FE phải đưa bảng về đủ 9 cột theo MH-03.3.

Re-verify chạy đúng Precondition ghi trong khối "CÁCH VERIFY sau Dev fix" của cột DEV phản hồi lần 2.

| Điều kiện | Bug gốc / CÁCH VERIFY yêu cầu | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản | `cbnv_tw` / Test@1234 | `cbnv_tw` — badge header "CB Nghiệp vụ - Trung ương / CB_NV_TW", đơn vị BTP · TW | Không |
| Môi trường | https://18.143.165.120.nip.io | Đúng env đó | Không |
| Màn hình | Đào tạo, tập huấn → Kho tài liệu / Bài giảng | Đúng màn đó, vào bằng click sidebar | Không |
| Bộ lọc ban đầu | Giữ bộ lọc mặc định (không lọc gì) khi đọc header | Đọc header ở trạng thái mặc định, chưa đụng bộ lọc; sau bước 4 đã bấm "Xóa bộ lọc" trả về mặc định | Không |
| Dữ liệu bước 2: bài giảng CÓ ảnh + CÓ lĩnh vực | Chưa có thì tự tạo qua [+ Thêm mới] | 5 bản ghi cũ đều không có ảnh → tự tạo qua [+ Thêm mới] bản ghi "QA R4 QLKTLBG_02 - Bai giang co anh va linh vuc" (PDF, ảnh PNG 200×200, lĩnh vực "Sở hữu trí tuệ") đúng như CÁCH VERIFY cho phép | Không |
| Dữ liệu bước 3: bài giảng KHÔNG ảnh + KHÔNG lĩnh vực | 1 bản ghi | Kiểm 2 bản ghi: "QA — STP-AG bài giảng nội bộ" (PDF) và "QA UAT Video QLKTLBG_08c" (Video) — nhiều hơn yêu cầu, phủ 2 loại tài liệu khác nhau | Không |
| Bước 4: lọc theo 1 lĩnh vực cụ thể | 1 lĩnh vực | Chạy 2 lần: "Sở hữu trí tuệ" và "Thuế" | Không |
| Bước 5: bấm vào ô cột Công khai | 1 dòng bất kỳ | Bấm ô "Đã công khai" của dòng "QA UAT Bài giảng Công khai QLKTLBG_08b"; phóng khổ màn lên 1920px để cột "Thao tác" dính hết chồng lên vùng cột Công khai rồi mới bấm, tránh trúng nhầm icon Sửa | Không |
| Cách đọc kết quả | Không kết luận chỉ bằng header (bẫy c) | Query DOM `.ant-table-thead th` + đọc từng `td`; kiểm thẻ `img` có `complete=true`, `naturalWidth=200`, `naturalHeight=200` chứ không chỉ xem ô tồn tại | Không |
