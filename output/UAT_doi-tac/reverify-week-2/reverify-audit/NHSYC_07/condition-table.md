# Bảng đối chiếu điều kiện — NHSYC_07 (Chức năng Lưu nháp)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (CB_NV_TW) — hiển thị góc phải video | cbnv_tw — CB Nghiệp vụ - Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái | Form thêm mới hồ sơ vụ việc (chưa lưu) `/vu-viec/tao-moi` → sau khi Lưu nháp, bản ghi ở trạng thái "Mới tạo" (VV-BTP-TW-20260709-001) | Form thêm mới hồ sơ vụ việc (chưa lưu) `/vu-viec/tao-moi` → sau khi Lưu nháp, bản ghi ở trạng thái "Mới tạo" (VV-BTP-TW-20260712-002) | Không |
| Dữ liệu tiền đề | Đã chọn doanh nghiệp có sẵn (DNTN Đông Dương BCT) rồi nhập nội dung | Đã chọn doanh nghiệp có sẵn (Công ty TNHH Seed Publishable) rồi nhập nội dung | Không |
| Input / giá trị nhập | 2 nhánh: (a) bấm "Lưu nháp" khi còn thiếu trường bắt buộc → hiện lỗi bắt buộc; (b) điền đủ rồi "Lưu nháp" → lưu thành công | 2 nhánh y hệt: (a) bấm "Lưu nháp" trên form trống → 5 lỗi bắt buộc; (b) điền đủ (DN + Tiêu đề + Nội dung + Lĩnh vực + Loại hình) rồi "Lưu nháp" → lưu thành công | Không |

**Kết luận:** 0 GAP — tái hiện đúng vai trò, đúng màn, đúng cả 2 nhánh mà đối tác đã chạy.
