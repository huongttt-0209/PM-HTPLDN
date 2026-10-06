# Condition table — BUG-EM-VV-002 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| SLA VU_VIEC gốc: 15 ngày, ngưỡng 50/100%, hệ số 2, email + in-app đều bật; hồ sơ `VV-STP-HN-20260821-001` ở `BINH_THUONG` | Ghi baseline trước job | Hồ sơ chưa có cảnh báo; CBNV HN chưa có thông báo entity; MailHog 3061 | Đúng baseline lúc 04:41Z | PASS |
| Tạm hạ ngưỡng 1 về 1% (version 17 → 18) | Chờ job SLA định kỳ 05:00Z | Hồ sơ đổi `BINH_THUONG → SAP_HET_HAN` | Job cập nhật hồ sơ lúc 05:00:00.163Z, version 2 → 3, `mucDoCanhBao=SAP_HET_HAN` | PASS |
| Người tiếp nhận `cbnv_hn` (`87bb5785-...`) | Đọc thông báo sau job | Có in-app cảnh báo sắp hết hạn | Có thông báo `7aa5b7c2-27cf-4aaa-9d2d-275ce79d6f0b` lúc 05:00:00.188Z | PASS |
| Kênh email đang bật | Quét MailHog từ 05:00:00Z | Email cảnh báo gửi đúng CBNV phụ trách | Thư lúc 05:00:00.272Z tới `diupt01+cb-nv-dn@gmail.com`; bản ghi in-app có `daGuiEmail=true`, cùng địa chỉ nhận | PASS |
| Sau phép thử | Hoàn nguyên cấu hình SLA | Trở lại đầy đủ giá trị gốc | Đã khôi phục 15 ngày, 50/100%, hệ số 2, 5 ngày bổ sung, hai kênh bật; version 19 lúc 05:01:26Z | PASS |

## Bằng chứng

- [In-app cảnh báo SLA](../bug-report/image/bug-em-vv-002-r3-inapp-sla-warning-2026-08-25.png) — SHA-256 `105b5cc192411bde1ee02c28232631075806900e8c4edb2afdf4c1a09bc2c01b`.
- [MailHog có email cảnh báo SLA](../bug-report/image/bug-em-vv-002-r3-mailhog-sla-warning-2026-08-25.png) — SHA-256 `f10a27516ea2908a026114811b48ce38430ae62049e12887ffc21ec1177e200e`.
- Do cấu hình SLA là toàn cục, cùng job còn gửi một cảnh báo hợp lệ cho `cbnv_tw_02`; kết quả mục tiêu HN được định danh riêng bằng entity ID và người nhận.

Kết luận R3: **PASS** — khi vụ việc chuyển mức cảnh báo, hệ thống gửi đủ in-app và email theo cấu hình.
