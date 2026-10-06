# Bảng đối chiếu điều kiện — QLTVV_22 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Màn hình | Form Thêm mới TVV, có thay đổi chưa lưu | Đã nhập Họ tên, CMND, Số QĐ, Giới tính | Không |
| Thao tác | Bấm Hủy → hộp xác nhận → chọn "Ở lại" | Hủy → hộp "Bạn có thay đổi chưa được lưu" → bấm "Ở lại" | Không |
| Kết quả kỳ vọng | Ở lại biểu mẫu, GIỮ NGUYÊN dữ liệu đã nhập | Vẫn ở form, dữ liệu giữ nguyên (Họ tên="QA Test OLai Retain", CMND="099999123456", Số QĐ="SQD-OLAI-2126", Giới tính=Nam) | Không |
