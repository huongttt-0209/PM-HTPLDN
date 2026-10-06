## [UAT_TGPL Doanh Nghiệp-tuần 2] row 128 — QLHSVV_07 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Tải tệp
Điều kiện: 1. Đăng nhập tài khoản 
2. Tồn tại bản ghi chứa tệp đính kèm
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Vụ việc HTPL"
2. Tìm kiếm và nhấn nút Chỉnh sửa tại dòng bản ghi
3. Bấm "Tải"
KQ mong đợi: Hệ thống tải tệp về máy người dùng.
KQ thực tế (l1): Nhấn vào biểu tượng "Tải xuống" hệ thống hiển thị màn hình xem chi tiết
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: Reopen
--- NOTE (Y: DEV phản hồi lần 2) ---
✅ Vẫn còn lỗi — chưa đạt.
- Đã kiểm lại trên bản dựng mới nhất của môi trường nghiệm thu, bằng tài khoản Cán bộ nghiệp vụ Trung ương, tại nhóm "Tài liệu đính kèm" trên màn hình Chi tiết vụ việc. Không chỉ nhìn hai biểu tượng, mà bấm lần lượt cả nút "Xem" lẫn nút "Tải" trên từng hàng tệp, rồi mở thư mục Tải xuống kiểm tệp thật.
- Phần đã hết lỗi: với tệp được thêm bằng nút "Thêm tài liệu" ở màn hình chi tiết, hai nút đã tách bạch đúng như mô tả. Bấm "Xem" mở khung xem trước ngay trong trang, bấm "Tải" thì tệp về máy và màn hình đứng nguyên, không mở màn xem nào. Chúng tôi kiểm 9 tệp thuộc nhóm này (ảnh JPG, tệp PDF, Word, Excel) trên 3 hồ sơ khác nhau, kể cả hồ sơ cũ ngày 03/08 và 30/06: cả 9 tệp đều tải về được, tệp nhận được trùng khít từng byte với tệp gốc.
- Phần còn lỗi: với tệp mà người dùng đính kèm ngay lúc tạo hồ sơ, bấm "Tải" không có tệp nào về máy, phần mềm chỉ hiện thông báo "Không kết nối được máy chủ." Bấm "Xem" cũng không mở được. Ngay trên bảng, hàng tệp đó cũng đã mất thông tin: tên tệp bị thay bằng chuỗi ký tự "File đính kèm 8e7566a5", cột Định dạng bỏ trống, cột Kích thước chỉ hiện dấu gạch ngang.
- Đo được: chúng tôi tự tạo hồ sơ mới VV-BTP-TW-20260804-005 qua đúng luồng thao tác của người dùng, đính kèm một tệp PDF 633 byte. Trên biểu mẫu trước khi lưu, tệp vẫn hiện đúng tên và đúng dung lượng; nhưng sau khi lưu thì thành hàng tệp không tên, không định dạng, không tải về được. Khi phần mềm đi lấy tệp về, hệ thống lưu trữ trả lời là không tìm thấy tệp này — tức tệp chưa hề được cất vào kho.
- Đã loại trừ khả năng do đường truyền hay do kho lưu trữ trục trặc: trong cùng vài phút đó, 9 tệp thuộc nhóm "Thêm tài liệu" vẫn tải về bình thường, chỉ nhóm tệp đính kèm lúc tạo hồ sơ là hỏng.
- Đã loại trừ khả năng do cách chúng tôi thao tác: lỗi lặp lại ở 4 hồ sơ khác nhau (VV-BTP-TW-20260804-001, -002, -003 và -005), trong đó hai hồ sơ đầu không phải do chúng tôi tạo.
- Vì yêu cầu của phiếu là bấm "Tải" thì tệp phải về máy người dùng, mà đúng những tệp doanh nghiệp gửi kèm ngay từ đầu lại không bao giờ lấy lại được, nên phần sửa mới đạt một phần.
- Ngoài ra, câu thông báo "Không kết nối được máy chủ." không đúng bản chất sự việc: máy chủ vẫn trả lời bình thường, vấn đề là tệp không có trong kho. Câu này khiến người dùng hiểu nhầm là lỗi mạng và ngồi thử lại nhiều lần.

— DEV 04/08/2026: ĐÃ FIX + VERIFY 120 PASS (V1.0.6).
- Root cause: createManual/createForDn/boSung lưu fileId UUID vào duong_dan_file thay vì object key MinIO, đồng thời dùng tên placeholder và bỏ trống metadata.
- Fix: resolve metadata trước khi lưu; ghi đúng tên/object key/định dạng/kích thước; link orphan VU_VIEC; chặn file thiếu hoặc khác đơn vị; áp dụng chung các luồng tạo thủ công, DN gửi, bổ sung và thêm tài liệu. Migration RepairVuViecAttachmentMetadata2026080400040 backfill dữ liệu cũ dưới RLS.
- Commit 2ab3dde0e; PR #81 merge 9fb8df697 vào dev; deploy 120 thành công, version giữ 1.0.6.
- Verify 120: hai hồ sơ cũ VV-BTP-TW-20260804-001/-002 được phục hồi và tải HTTP 200. Hồ sơ tạo mới VV-BTP-TW-20260804-003: upload/create 201; UI hiện đúng tên PDF, 329 B, Sạch; Tải HTTP 200; SHA-256 nguồn và tệp tải trùng fb0f4ddb48d12cc80b8da22356b9f0faab1a18470382f709f19b6e7ea5a2888a.
- Bằng chứng: QLHSVV_07-reopen-120-after-deploy.png.