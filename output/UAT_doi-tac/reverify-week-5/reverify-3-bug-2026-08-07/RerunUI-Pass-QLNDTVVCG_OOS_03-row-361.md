# Re-run UI bug QLNDTVVCG_OOS_03 — dòng 361

- Môi trường: `https://18.143.165.120.nip.io` — HTPLDN v1.0.10
- Ngày chạy: 07/08/2026 (Asia/Ho_Chi_Minh)
- Công cụ thao tác: Chrome DevTools trên cửa sổ Chrome hiển thị
- Tài khoản phân công: `cbnv_tw_01`
- Chuyên gia nhận: `qa_tvvseed28`
- Bản ghi: `TVCS-20260806-0003`
- Verdict: **PASS**

## Luồng UI đã chạy

1. Đăng nhập `cbnv_tw_01` trên UI và nhập OTP đọc trực tiếp từ MailHog UI.
2. Mở menu **Tư vấn chuyên sâu**, chọn hồ sơ `TVCS-20260806-0003` đang ở trạng thái **Tiếp nhận**.
3. Mở modal phân công, chọn `QA TVV Seed28 Active`, nhập ghi chú và nhấn **Phân công**.
4. Quan sát danh sách đổi sang **Đã phân công**.
5. Mở MailHog UI, đọc email nghiệp vụ vừa sinh.
6. Đăng xuất trên UI, đăng nhập `qa_tvvseed28`, mở chuông thông báo và đọc notification mới nhất.

## Kết quả

- MailHog tăng `1949 → 1950` ngay sau thao tác phân công.
- Email gửi đúng người nhận `qa.tvvseed28@htpldn-uat.local`.
- Tiêu đề email: `Bạn được phân công tư vấn: TVCS-20260806-0003`.
- Nội dung email có mã yêu cầu, nội dung yêu cầu và SLA: chuyên gia xác nhận trong **2 ngày làm việc**, quá hạn hệ thống tự thu hồi.
- Chuông thông báo của `qa_tvvseed28` hiển thị bản tin loại `PHAN_CONG` với đúng tiêu đề và mã `TVCS-20260806-0003`.
- Email OTP đăng nhập chuyên gia sinh sau đó được tách riêng, không dùng làm bằng chứng nghiệp vụ.

## Kết luận

Bug đã được fix thành công trên luồng UI thực tế: thao tác phân công sinh đủ **in-app notification + email**. Không ghi `Kết quả verify` vì verdict Pass.
