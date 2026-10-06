# Condition table — BUG-EM-INF-002 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| MailHog baseline `3028` lúc `2026-08-25T04:06:36.235Z`; vụ việc `VV-BTP-TW-20260805-001` ở `DA_TIEP_NHAN` | Phân công `TO_CHUC` cho `TCTV-SEED-0001` và TVV `TVV-BTP-TW-0002` | API 201, vụ việc chuyển `DA_PHAN_CONG` | 201; version 3 → 4; `loaiDoiTuongXuLy=TO_CHUC` | PASS |
| TVV có email `diupt01+cg@gmail.com`; tổ chức có email `diupt01+org-a@gmail.com` | Quét thư phát sinh sau baseline | Một thư duy nhất: TVV ở `To`, tổ chức ở `Cc` | Tổng mailbox 3028 → 3029; đúng 1 thư lúc `04:06:43.601Z`; `To=[diupt01+cg@gmail.com]`, `Cc=[diupt01+org-a@gmail.com]`, `Bcc=[]` | PASS |
| Cùng cửa sổ phát thư | Đối chiếu SMTP recipients và `Message-ID` | Không tách thành hai thư độc lập | Một `Message-ID` `<ef7d10fd-aa53-97e1-d323-4d44196c8c4a@htpldn.staging>`; `Raw.To` chứa cả TVV và tổ chức | PASS |
| Cùng cửa sổ phát thư | Kiểm mailbox âm | Tổ chức/TVV khác không nhận | Không có thư thứ hai hoặc recipient ngoài hai địa chỉ đúng | PASS |

**Kết luận:** PASS — email phân công qua tổ chức đã dùng một thư với TVV ở `To` và điểm liên hệ tổ chức ở `Cc`.

**Evidence:** [MailHog API message](../bug-report/image/bug-em-inf-002-r3-single-message-to-cc-2026-08-25.png) — SHA-256 `b7b99db7a79a0e35a1cbc5056aa3465e6f4592ec078aa0abefd26f8496b13e1f`.
