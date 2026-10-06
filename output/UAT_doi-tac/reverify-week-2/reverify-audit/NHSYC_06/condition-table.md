# Bảng đối chiếu điều kiện — NHSYC_06 (Tệp đính kèm vi phạm quy định)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (CB_NV_TW) — hiển thị góc phải ảnh | cbnv_tw — CB Nghiệp vụ - Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái | Form thêm mới hồ sơ vụ việc (chưa lưu), URL `/vu-viec/tao-moi`, nhóm "Tài liệu Đính kèm" | Form thêm mới hồ sơ vụ việc (chưa lưu), URL `/vu-viec/tao-moi`, nhóm "Tài liệu Đính kèm" — cùng màn | Không |
| Dữ liệu tiền đề | Vùng đính kèm còn trống, chú thích "Tối đa 10 tệp… Dung lượng tối đa: 20MB" | Vùng đính kèm còn trống, chú thích y hệt | Không |
| Input / giá trị nhập (tệp vi phạm) | Ảnh chỉ chụp chú thích vùng đính kèm, **không thấy đối tác thực sự tải tệp vi phạm nào** | Tự tải tệp vi phạm thật, đủ **4 loại vi phạm** theo SRS: (1) sai định dạng `.txt`; (2) vượt 20MB/tệp — PDF 25MB; (3) vượt 10 tệp — tải tệp thứ 11; (4) vượt tổng 100MB — 6 tệp × 18MB = 108MB | Không |

**Kết luận:** 0 GAP. Cùng vai trò, cùng màn, cùng vùng chức năng. Đối tác chỉ chụp chú thích chứ chưa tải tệp vi phạm; mình đã **tự chạy đủ 4 nhánh vi phạm** mà SRS quy định để kiểm tra hệ thống có chặn + báo lỗi không.
