# Condition table — BUG-EM-HDD-001 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Hồ sơ đúng luồng | `DANG_XU_LY → CHO_PHE_DUYET` sau gửi phản hồi | `HD-20260824-003`, id `3ce3f157-06ab-423f-b0db-5cd28fc70826`, lịch sử có `SUBMIT` lúc `2026-08-24T10:57:34.331Z`; trạng thái hiện tại `CHO_PHE_DUYET` | Không |
| In-app CBPD | Tạo thông báo phê duyệt | id `40fb5b8b-a1c4-4c22-bcf8-ac816bda94dc`, tiêu đề “Phản hồi mới cần phê duyệt”, lúc `10:57:34.434Z` | Không |
| Email CBPD | Phát email cùng sự kiện | MailHog id `vY954QF34q08qw4pGSRP_Uv6Dc-w0TLO3oZgdeDl-ts=@mailhog.example`, tới `diupt01+cb-pd-a@gmail.com` lúc `10:57:34.520Z` | Không |
| Độ trễ | SLA email ≤ 5 phút | Email sau in-app khoảng 86 ms | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16; MailHog `http://18.143.165.120:8025` | Không |

**Kết luận:** PASS — sự kiện gửi phản hồi đã phát đồng thời in-app và email cho Cán bộ Phê duyệt cùng đơn vị.
