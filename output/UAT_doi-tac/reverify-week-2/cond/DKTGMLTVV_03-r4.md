# Bảng đối chiếu điều kiện — re-verify DKTGMLTVV_03 (row 53, mode reverify2, 30/07/2026)

Bug gốc (vòng 2): form đăng ký tư vấn viên gom nhóm sai (6 nhóm, "Quyết định công bố" tách riêng) và
2 trường Chuyên ngành / Số năm kinh nghiệm không bắt buộc ở luồng đăng ký mới. BA chốt 30/07/2026:
gộp về 5 nhóm + đưa Số QĐ/Ngày QĐ công bố vào nhóm 2; bắt buộc 2 trường ở FR-IV-03 nhưng KHÔNG bắt
buộc ở luồng sửa FR-IV-04; bỏ bắt buộc Tổ chức hành nghề chính (tư vấn viên tự do).

| Điều kiện | Bug gốc / CÁCH VERIFY yêu cầu | Mình test | GAP? |
|---|---|---|---|
| Tài khoản luồng đăng ký mới | `nht_qa_tw` / Test@1234 (Người hỗ trợ, Cục Bổ trợ tư pháp - BTP) | Đúng `nht_qa_tw`, đăng nhập lần đầu thành công, không phải dùng account dự phòng | Không |
| Tài khoản luồng sửa hồ sơ cũ | `cbnv_tw` / Test@1234 (Cán bộ Nghiệp vụ TW) | Đúng `cbnv_tw`, đăng nhập lần đầu thành công | Không |
| Màn hình | Mạng lưới tư vấn viên → Tư vấn viên/Chuyên gia → tab "Mới đăng ký" → [Thêm mới] | Đúng màn đó | Không |
| Loại hồ sơ ở bước 3 | Loại = Tư vấn viên | Đúng Loại = Tư vấn viên | Không |
| Dữ liệu bước 3 (điền đủ trường bắt buộc khác, chỉ để trống 2 trường cần kiểm) | Để trống đúng Chuyên ngành + Số năm kinh nghiệm | Điền đủ 8 trường bắt buộc còn lại (Họ tên, Ngày sinh 10/10/1992, Giới tính, CCCD 048200030744, Email, SĐT, Địa chỉ, Trình độ Thạc sĩ, Lĩnh vực, Tổ chức Seed) + tệp thẻ hành nghề; chỉ để trống đúng 2 trường cần kiểm | Không |
| Giá trị bước 4 | Chuyên ngành "Luật Kinh tế", Số năm kinh nghiệm 5 | Đúng 2 giá trị đó → tạo ra TVV-BTP-TW-0023 | Không |
| Bước 4 phải mở lại hồ sơ để kiểm (bẫy c) | Không được dừng ở thông báo lưu thành công | Mở lại chính TVV-BTP-TW-0023 đọc trực tiếp 2 ô; kiểm 2 lần bằng 2 tài khoản khác nhau | Không |
| Bước 5 | Để trống Tổ chức hành nghề chính trên form Thêm mới | Đúng vậy → tạo ra TVV-BTP-TW-0024 "QA R4 DKTGMLTVV03 Buoc5 TuDo", cột Tổ chức trong danh sách hiện "—" | Không |
| Bước 6 phải là hồ sơ ĐÃ CÓ, luồng SỬA (bẫy b) | `cbnv_tw` bấm [Sửa] hồ sơ đã có → xóa trắng Chuyên ngành | Sửa hồ sơ đã có TVV-BTP-TW-0023, xóa trắng Chuyên ngành, lưu được; hai nhãn Chuyên ngành / Số năm kinh nghiệm trên màn Sửa đều không có dấu sao | Không |
| Cách kết luận bước 3 (bẫy d) | Phải bấm Lưu thật, không xét riêng dấu sao | Đã bấm Lưu thật; kết luận dựa trên việc vẫn đứng ở form kèm đúng 2 báo lỗi và không sinh bản ghi nào | Không |
