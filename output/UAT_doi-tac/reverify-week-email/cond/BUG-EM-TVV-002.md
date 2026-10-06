# Condition table — BUG-EM-TVV-002 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| `cbnv_tw_01`; TVV `TVV-BTP-TW-0051` (`b9ecc5d1-2e14-4db8-adfc-aae5778f307d`) cùng đơn vị, trạng thái `MOI_DANG_KY`, version 1 | `POST /bat-dau-tham-dinh` | Hồ sơ sang `DANG_THAM_DINH` | API 200, version 2, trạng thái `DANG_THAM_DINH` lúc 04:33:13Z | PASS |
| Hồ sơ đang thẩm định; MailHog baseline 3043 thư | Gửi kết luận `DAT`, `trinhDuyet=true`, 4 nhóm tiêu chí hợp lệ | Hồ sơ sang `CHO_PHE_DUYET`; CBPD cùng đơn vị nhận in-app + email | API 200 lúc 04:33:19Z, version 3 và `CHO_PHE_DUYET` | PASS |
| Tài khoản `cbpd_tw_01` | Đọc thông báo vừa sinh | Có thông báo phê duyệt và trạng thái gửi email thành công | Thông báo `11df56e3-c441-4491-8614-01755e2b39f9`, `daGuiEmail=true`, `emailNhan=diupt01+cb-pd-a@gmail.com`, `ngayGuiEmail=04:33:19.954Z` | PASS |
| MailHog sau trigger | Quét toàn bộ thư từ 04:33:19Z | Chỉ các CBPD cùng đơn vị nhận thư | Có đúng 6 thư “Hồ sơ TVV chờ phê duyệt” tới `cbpd_tw`, `cbpd_tw_03`, `cbpd_tw_04`, `cbpd_tw_05`, `diupt01+cb-pd-a@gmail.com`, `diupt01+cb-pd-a-2@gmail.com`; không có CB NV | PASS |

## Bằng chứng

- [MailHog — đúng 6 thư CBPD cùng đơn vị](../bug-report/image/bug-em-tvv-002-r3-six-cbpd-emails-2026-08-25.png) — SHA-256 `359cde72a3bedffd5a0e4040f2ba81a4db757efef0ec60a10f8f167f3088fccf`.
- Fixture QA được giữ ở `CHO_PHE_DUYET` để không phát sinh thêm thông báo từ chối ngoài phạm vi phép thử.

Kết luận R3: **PASS** — sự kiện trình duyệt hồ sơ TVV đã gửi đủ in-app và email cho CBPD cùng đơn vị.
