# Audit — NHSYC_OOS_01 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`, row 131)

**Case:** Nhập hồ sơ vụ việc thủ công — một lần bấm nút lưu rơi vào nhánh lỗi sinh HAI khung thông báo cùng lúc
**Verdict QA vòng 1:** `Open` (cột `Verify` / Q)

## Phản hồi dev bị QA đè khi đồng bộ cột P (2026-08-03)

> **Bối cảnh:** ngày 03/08/2026 QA đồng bộ cột `Trạng thái dev fix 1` (P) của row 131 về đúng verdict QA (`Open`).
> Mode `verify1` của `tools/sheet_write.py` ghi cặp ô **P + R**, nên nội dung cũ của cột R — vốn là **phản hồi của DEV**,
> không phải note QA — bị ghi đè. Chép nguyên văn giá trị đọc live từ ô `R131` ngay trước lần ghi để không mất dấu vết.

**Nguyên văn ô `R131` (cột "DEV phản hồi lần 1") trước khi bị đè — 166 ký tự:**

```text
Đã fix: 1 request lỗi = 1 toast (bỏ toast thủ công ở catch, để hook onError là nguồn duy nhất). Commit a69f48fc3. Verify local 3/3 + 120 (MutationObserver = 1 toast).
```

**Xử lý của QA:** note mới ghi đè vào R131 giữ nguyên phần mô tả lỗi của QA và **bổ sung 1 gạch đầu dòng cuối**
ghi nhận việc phía phát triển đã báo sửa xong, đồng thời nêu rõ tổ kiểm thử **chưa kiểm tra lại bản sửa** nên
trạng thái tạm giữ ở mức chưa đạt, sẽ xác nhận ở lượt kiểm tra kế tiếp. Note gửi đối tác không nhắc số commit /
tên hàm / tên biến (thông tin nội bộ) — các chi tiết đó chỉ lưu ở file audit này.
