# Các nội dung cần BA xác nhận — UAT đối tác tuần 2

## GHSYCHTPL_02 — Hiển thị Tên doanh nghiệp/MST trên form gửi yêu cầu

### Hiện trạng UAT

- Form `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý` đã bỏ khối “Thông tin người gửi”.
- Form đã bỏ “Độ ưu tiên” và “Lý do ưu tiên”; hệ thống tự tính ưu tiên theo thông tin DN.
- Form không hiển thị Tên doanh nghiệp và Mã số thuế.

### Căn cứ SRS

- FR-V.I-02 (UC52) dòng 179: `doanh_nghiep_id` lấy từ phiên DN đã đăng nhập, không nhập thủ công.
- Dòng 187: thông tin DN được đọc từ DOANH_NGHIEP theo `doanh_nghiep_id`.
- SRS chưa có điều khoản/thành phần màn hình nói rõ phải hiển thị Tên doanh nghiệp và Mã số thuế ở dạng chỉ đọc trên form DN.

### Cần BA chốt

1. **Có hiển thị:** bổ sung Tên doanh nghiệp và Mã số thuế dạng chỉ đọc vào FR/mô tả màn hình, rồi chuyển dev thực hiện.
2. **Không hiển thị:** giữ UAT hiện tại, chỉ lấy doanh nghiệp từ phiên đăng nhập; phản hồi đối tác điều chỉnh kỳ vọng.

Hai nội dung “Thông tin người gửi” và “Độ ưu tiên/Lý do ưu tiên” đã phù hợp SRS, không còn cần xử lý.

### Bằng chứng

- Audit: `reverify-audit/GHSYCHTPL_02-UAT-2026-08-12.md`.
- Ảnh UAT: `reverify-audit/GHSYCHTPL_02-UAT-form-top.png`.
