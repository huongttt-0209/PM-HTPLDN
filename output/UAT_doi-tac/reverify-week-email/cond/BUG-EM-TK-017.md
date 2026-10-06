# Condition table — BUG-EM-TK-017 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| DN `0109998887`: `TAI_KHOAN.email=diupt01+dn-login@gmail.com`; `DOANH_NGHIEP.email=diupt01+dn-contact@gmail.com`; baseline 9 và 8 thư | Công khai `VV-BTP-TW-20260814-002` (version 13) | Workflow mail tới TAI_KHOAN.email | API 200; account mailbox 9 → 10; contact mailbox giữ 8 | PASS |
| Vụ việc đang công khai | Hủy công khai với lý do hợp lệ (version 14) | Workflow mail tiếp tục tới TAI_KHOAN.email | API 200; account mailbox 10 → 11; contact mailbox giữ 8 | PASS |
| Hai thư R3 | Kiểm `To`, `Raw.To`, Cc/Bcc | Chỉ định tuyến tới account email | `To` và `Raw.To` chỉ `diupt01+dn-login@gmail.com`; không Cc/Bcc sang contact | PASS |
| Kết thúc kiểm tra | Đối chiếu trạng thái vụ việc | Hoàn nguyên `congKhai=false` | Version 15, `congKhai=false` | PASS |

**Kết luận:** PASS — workflow vụ việc đã gửi tới `TAI_KHOAN.email`, không còn gửi tới email liên hệ của doanh nghiệp.

**Evidence:** [MailHog API message](../bug-report/image/bug-em-tk-017-r3-workflow-to-account-email-2026-08-25.png) — SHA-256 `2d7fc12d30f21b15e6be8cf59adc8366b35a5e48bcef8fda0f4810b0a83f913c`.
