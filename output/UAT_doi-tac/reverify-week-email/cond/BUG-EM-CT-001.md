# Condition table — BUG-EM-CT-001 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Người thao tác | `CB_NV_TW`, cùng đơn vị với cán bộ phê duyệt | `cbnv_tw_01`, đơn vị BTP-TW | Không |
| Người nhận | `CB_PD_TW`, cùng đơn vị | `cbpd_tw_01`, email `diupt01+cb-pd-a@gmail.com`, đơn vị BTP-TW | Không |
| Hồ sơ / trạng thái đầu | `CT-SEED-106`, `DANG_THAM_DINH`, kết quả thẩm định Đạt | Đưa `CT-SEED-106` về Đang thẩm định bằng luồng Trả về thẩm định; kết quả Đạt được giữ nguyên | Không |
| Hành động | Trình phê duyệt | Xác nhận Trình phê duyệt lúc 10:04:55 (UTC+7), POST thành công | Không |
| Trạng thái sau | `CHO_PHE_DUYET` | UI hiển thị Chờ phê duyệt | Không |
| Thông báo trong ứng dụng | Cán bộ phê duyệt nhận thông báo | Bản ghi mới `978e2cb2-2dd4-4ff0-8f99-284b0fee0dc3`, tạo lúc `2026-08-25T03:04:55.366Z` | Không |
| Email | Gửi email cho cán bộ phê duyệt cùng đơn vị | Tổng MailHog `2997 → 3003`; hộp `cbpd_tw_01` `48 → 49`; subject “Hồ sơ chi trả CT-SEED-106 cần phê duyệt” | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16; MailHog `18.143.165.120:8025` | Không |

**Kết luận:** PASS — lỗi đã được khắc phục, hai kênh in-app và email đều phát sinh đúng sau thao tác Trình phê duyệt.
