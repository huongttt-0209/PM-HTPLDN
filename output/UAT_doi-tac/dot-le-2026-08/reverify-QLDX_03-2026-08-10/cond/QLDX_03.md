# Bảng đối chiếu điều kiện — QLDX_03 (re-verify 10/08/2026, env đối tác `htpldn-uat.ospgroup.vn`)

Loại claim: hộp thoại cảnh báo tự động khi không thao tác — phụ thuộc **thời gian idle**, độc lập vai trò/dữ liệu nghiệp vụ.

| Điều kiện có thể đổi kết quả | Bug gốc + TKM retest 31/7 | Mình test 10/08 | GAP? |
|---|---|---|---|
| Trạng thái phiên | Đã đăng nhập thành công | Đã đăng nhập thành công (`cbnv_tw` / CB_NV_TW, build **V1.0.10**) | Không |
| Thời gian không thao tác | ~25–30 phút không thao tác | Kẹp hai đầu ngưỡng 25′ (24:50 → không bật; 25:01 → tự bật); nhánh 30′ chạy 1 lượt **đồng hồ thật** (đặt 29:50 rồi để thật chạy tiếp 10s tới 30:00) | Không |
| Mốc idle có bị request nền ghi đè không | Không nêu trong phiếu | Đo im lặng 188s / 378 mẫu → `auth-last-activity` giữ **1 giá trị duy nhất**, 0 lần bị ghi đè | Không |
| Tình trạng mạng | Không nêu trong phiếu | Watchdog `curl` 25s/lần, **32/32 lần HTTP 200** liên tục 03:29:26–03:42:24 (phủ kín khoảng đo) → loại trừ rớt mạng | Không |
| Loại phiên | Phiếu không nêu; BA yêu cầu áp dụng cả "Ghi nhớ đăng nhập" | Test cả 2: phiên thường **và** phiên tick "Ghi nhớ đăng nhập" → cùng bật modal ở idle 1501s | Không |
| Kết quả quan sát được | Bug gốc: "không hiển thị hộp thoại cảnh báo dù idle 30 phút". TKM 31/7: "không hiện hộp thoại, chuyển thẳng màn Đăng nhập + *Đăng xuất thành công*" | Modal **"Phiên làm việc sắp hết hạn"** bật đúng phút 25, có đếm ngược thật + 2 nút **"Gia hạn phiên"/"Đăng xuất"**; phút 30 tự đăng xuất kèm thông báo **"Phiên làm việc đã hết hạn do không có thao tác"** (KHÔNG phải "Đăng xuất thành công") | Không |

**Kết luận: 0 GAP.** Không tái hiện được cả claim gốc lẫn triệu chứng TKM báo lại 31/7.

> **Khai rõ về cách rút ngắn thời gian:** không ngồi chờ đủ 25/30 phút mà đặt lại mốc `auth-last-activity`
> (chính là mốc mà FE đọc để đo idle) rồi để đồng hồ thật chạy qua ngưỡng. Đã đóng 3 chốt chống Pass oan:
> (1) chứng minh mốc không bị request nền ghi đè; (2) kẹp hai đầu 24:50/25:01 chứng minh có timer nền chạy
> chứ không phải chỉ phản ứng theo thao tác; (3) nhánh 30′ để đồng hồ thật tự chạm ngưỡng.
