# Condition table — BUG-EM-DG-001 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Người thao tác | `CB_NV_TW`, đơn vị BTP-TW | `cbnv_tw_01`, đơn vị BTP-TW | Không |
| Kế hoạch / trạng thái | Kế hoạch ở trạng thái Phân công, bộ tiêu chí tổng trọng số 100% và thang điểm 100 | `DG-20260730-0002`, trạng thái Phân công; 2 tiêu chí 60% + 40%, điểm tối đa 100 | Không |
| Người được phân công | Người đánh giá cùng đơn vị, email `diupt01+cg@gmail.com` | `QA TVV Seed28 Active` (`5432719c-c542-4a5d-8c3a-db1b8a918bbf`), BTP-TW, email đúng | Không |
| Hành động / dữ liệu lưu | Thêm với vai trò Đánh giá viên | Bản ghi `917795c0-caa3-45e5-9495-9d18b535ffad` được tạo lúc `2026-08-25T03:14:54.121Z`, vai trò `DANH_GIA_VIEN` | Không |
| Thông báo trong ứng dụng | Người được phân công nhận thông báo | Bản ghi `2e3ea426-241f-45ad-8b32-4e5af1f473f2`, tạo lúc `2026-08-25T03:14:56.250Z`, tiêu đề “Bạn được phân công đánh giá - DG-20260730-0002” | Không |
| Email | Gửi đúng 1 email cho người được phân công | Tổng MailHog `3003 → 3004`; hộp `diupt01+cg@gmail.com` `22 → 23`; email tạo lúc `2026-08-25T03:15:10.955Z` | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16; MailHog `18.143.165.120:8025` | Không |

**Kết luận:** PASS đối với triệu chứng gốc — người được phân công đã nhận đúng cả in-app và email.

**Ghi nhận ngoài triệu chứng gốc:** request UI bị `net::ERR_ABORTED` sau khoảng 10 giây và hiện toast “Thêm người đánh giá thất bại”, dù bản ghi đã lưu và hai kênh thông báo đã được phát. Hiện tượng này cần được theo dõi riêng, không phải triệu chứng thiếu thông báo của `BUG-EM-DG-001`.
