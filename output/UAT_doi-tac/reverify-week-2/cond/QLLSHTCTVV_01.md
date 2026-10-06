# Bảng đối chiếu điều kiện — re-verify QLLSHTCTVV_01 (row 81)

Bug gốc (Reopen lần trước): thẻ "Lịch sử hỗ trợ" của TVV hiển thị cột "Ngày hoàn thành" = "Invalid Date"
cho vụ việc CHƯA hoàn thành (phải để trống hoặc "—"). Re-test 2026-07-15: mở đúng TVV + thẻ Lịch sử hỗ trợ,
kiểm cột "Ngày hoàn thành" của vụ việc chưa hoàn thành.

| Điều kiện | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản | CB Nghiệp vụ Trung ương (`cbnv_tw` — CB_NV_TW) | Đăng nhập `cbnv_tw` (CB_NV_TW) | Không |
| Entity TVV + trạng thái | TVV-BTP-TW-0002 (QA TVV Seed28 Active), "Đang hoạt động" | TVV-BTP-TW-0002 (QA TVV Seed28 Active), "Đang hoạt động" | Không |
| Dữ liệu tiền đề (vụ việc chưa hoàn thành) | VV-BTP-TW-20260712-001 ở "Đã phân công" (chưa hoàn thành), người xử lý = TVV này | VV-BTP-TW-20260712-001 "Đã phân công" (chưa hoàn thành) có mặt trong Lịch sử hỗ trợ + 2 vụ việc chưa hoàn thành khác (Đã hoàn thành = 0) | Không |
| Bộ lọc | Không đặt bộ lọc nào | Không đặt bộ lọc nào (thẻ Lịch sử hỗ trợ mặc định) | Không |
