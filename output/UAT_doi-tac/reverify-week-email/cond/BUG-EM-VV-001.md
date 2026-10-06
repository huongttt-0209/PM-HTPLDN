# Condition table — BUG-EM-VV-001 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| Vụ việc `VV-BTP-TW-20260803-002` thuộc DN `0109998887`; đã đi đúng workflow tới `DA_DUYET`, version 7 | Ghi baseline tài khoản DN và MailHog | Chưa có thông báo cho entity này; MailHog 3059 thư | DN có 0 thông báo cho entity; baseline MailHog 3059 lúc 04:37:12Z | PASS |
| CBNV `cbnv_tw_01`, hồ sơ `DA_DUYET` | `POST /hoan-thanh` với kết luận cuối, `ketQuaXuLy=THANH_CONG`, version 7 | API thành công, hồ sơ sang `HOAN_THANH` | API 201 lúc 04:37:27Z, version 8, có `ngayHoanThanh` và kết luận đã lưu | PASS |
| Tài khoản DN `0109998887` đang hoạt động | Đọc chuông/API thông báo sau trigger | Có thông báo “Vụ việc đã hoàn thành” | Có đúng 1 bản ghi `a89a7598-f4d9-4eee-9cdd-6fbbf29461c0` lúc 04:37:27.850Z, `daGuiEmail=true` | PASS |
| MailHog sau trigger | Quét thư từ 04:37:27Z | Có email hoàn thành gửi đúng email đăng nhập DN | Có đúng 1 thư lúc 04:37:27.905Z tới `diupt01+dn-login@gmail.com`; tổng 3059 → 3060 | PASS |

## Bằng chứng

- [Chuông doanh nghiệp có thông báo hoàn thành](../bug-report/image/bug-em-vv-001-r3-dn-inapp-completed-2026-08-25.png) — SHA-256 `1281cafb636199cbdf447d3c17df0086cb5fda37515ca234d936a7b0829c4bdb`.
- [MailHog có thư hoàn thành](../bug-report/image/bug-em-vv-001-r3-mailhog-completed-2026-08-25.png) — SHA-256 `bd33b6b637d11d6985aef7980cb81c2694899ee155b9b2cf74e62a8bdfaf50b7`.

Kết luận R3: **PASS** — doanh nghiệp có tài khoản hoạt động đã nhận đủ in-app và email khi vụ việc hoàn thành.
