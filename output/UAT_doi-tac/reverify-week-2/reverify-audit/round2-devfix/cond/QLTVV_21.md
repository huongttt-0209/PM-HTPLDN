# Bảng đối chiếu điều kiện — QLTVV_21 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Thao tác | Thêm mới TVV hợp lệ: Ảnh chân dung .png + File thẻ hành nghề .pdf + File đính kèm .pdf + Số QĐ, bấm Lưu | Tạo TVV-BTP-TW-0009 đủ trường bắt buộc + avatar .png + thẻ hành nghề .pdf + File đính kèm test-02.pdf + Số QĐ "SQDCB-QA-2100/2126" → Lưu thành công (redirect danh sách) | Không |
| Ảnh chân dung .png | Bị từ chối "Chỉ chấp nhận file PDF", không lưu | Được chấp nhận (có preview khi tải, KHÔNG có lỗi "Chỉ chấp nhận file PDF"); lưu vào hồ sơ (màn Sửa hiện mục "Ảnh chân dung" + nút Xem) | Không |
| File đính kèm | Không gắn vào hồ sơ ("Chưa có file đính kèm") | Hồ sơ hiển thị File đính kèm "test-02.pdf (237 B)" + nút Xem/Tải | Không |
| Số quyết định | Đã nhập nhưng không hiển thị ("Số quyết định: —") | Chi tiết hiển thị "Số QĐ công bố: SQDCB-QA-2100/2126" | Không |
