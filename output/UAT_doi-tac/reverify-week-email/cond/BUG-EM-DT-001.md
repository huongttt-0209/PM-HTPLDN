# Condition table — BUG-EM-DT-001 (R4)

| Nhánh | Kỳ vọng theo SRS v3.5 | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Gửi phê duyệt CTĐT | Email tới CBPD cùng đơn vị | `CTDT-BTP-TW-2026-0006` chuyển `DU_THAO → CHO_DUYET` lúc 10:34; MailHog người nhận `diupt01+cb-pd-a@gmail.com` tăng 49→50, thư đến `03:34:54.743Z` | Không |
| Phê duyệt CTĐT | In-app + email tới **người tạo** | Người tạo thực tế là `cbnv_tw_02`; MailHog đúng hộp `diupt01+cb-nv-a-2@gmail.com` có thư phê duyệt `CTDT-BTP-TW-2026-0006` lúc `03:35:34.179Z` | Không |
| Thông báo trong ứng dụng sau phê duyệt | Có bản ghi cho người tạo | Phiên `cbnv_tw_02` trả in-app ID `7b963a3a-aa1a-4828-aca9-0ea4e47b73d4`, tiêu đề CTĐT đã được phê duyệt | Không |
| Gửi phê duyệt Khóa học | In-app + email tới CBPD cùng đơn vị | Fresh run `KH-20260822-001` lúc `07:32:54Z`: chuyển `DU_THAO → CHO_DUYET`; CBPD có in-app ID `23544ae7-5539-486d-895b-4c992e39a3c9`; MailHog đúng hộp tăng `55→56` | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16; MailHog `http://18.143.165.120:8025` | Không |

**Kết luận:** PASS / Closed-verified. R3 đếm sai tài khoản người tạo; khi đối chiếu đúng `cbnv_tw_02`, cả ba vế đều có đủ in-app + email theo BR-NOTIF-01.
