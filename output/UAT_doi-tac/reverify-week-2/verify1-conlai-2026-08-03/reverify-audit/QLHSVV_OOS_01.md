# Audit — QLHSVV_OOS_01 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`, row 133)

**Case:** Cột "Loại" của bảng tài liệu đính kèm trong hồ sơ vụ việc hiển thị mã nội bộ `BO_SUNG` thay vì nhãn tiếng Việt
**Verdict QA vòng 1:** `Open` (cột `Verify` / Q)

## Phản hồi dev bị QA đè khi đồng bộ cột P (2026-08-03)

> **Bối cảnh:** ngày 03/08/2026 QA đồng bộ cột `Trạng thái dev fix 1` (P) của row 133 về đúng verdict QA (`Open`).
> Mode `verify1` của `tools/sheet_write.py` ghi cặp ô **P + R**, nên nội dung cũ của cột R — vốn là **phản hồi của DEV**,
> không phải note QA — bị ghi đè. Chép nguyên văn giá trị đọc live từ ô `R133` ngay trước lần ghi để không mất dấu vết.

**Nguyên văn ô `R133` (cột "DEV phản hồi lần 1") trước khi bị đè — 134 ký tự:**

```text
Đã fix: cột "Loại" bảng tài liệu đính kèm map enum LoaiTaiLieu→nhãn VN (BO_SUNG→"Bổ sung"). Commit f9094d559. Verify local + 120 PASS.
```

**Xử lý của QA:** note mới ghi đè vào R133 giữ nguyên phần mô tả lỗi của QA và **bổ sung 1 gạch đầu dòng cuối**
ghi nhận việc phía phát triển đã báo sửa xong, đồng thời nêu rõ tổ kiểm thử **chưa kiểm tra lại bản sửa** nên
trạng thái tạm giữ ở mức chưa đạt, sẽ xác nhận ở lượt kiểm tra kế tiếp. Note gửi đối tác không nhắc số commit /
tên hàm / tên biến (thông tin nội bộ) — các chi tiết đó chỉ lưu ở file audit này.
