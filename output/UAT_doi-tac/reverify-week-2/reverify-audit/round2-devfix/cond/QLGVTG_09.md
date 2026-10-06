# Bảng đối chiếu điều kiện — QLGVTG_09 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Màn hình / state | Màn Sửa giảng viên đang có Lĩnh vực | Sửa GV "QA GV QLGVTG09", Lĩnh vực = Thuế | Không |
| Thao tác | Xóa (bỏ chọn) toàn bộ Lĩnh vực rồi bấm Lưu | Xóa tag "Thuế" → bấm Lưu | Không |
| Kết quả kỳ vọng | Một (1) thông báo lỗi cho trường Lĩnh vực | `.ant-form-item-explain-error` đếm được đúng 1 dòng "Vui lòng chọn ít nhất 1 lĩnh vực" | Không |
